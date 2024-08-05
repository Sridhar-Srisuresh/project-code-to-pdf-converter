from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Flowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from pdf_styler import get_styles


class WrappedCode(Flowable):
    def __init__(self, code):
        Flowable.__init__(self)
        self.code = code
        self.font_size = 10
        self.line_height = 11

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        lines = self.code.split('\n')
        self.wrapped_lines = []
        for line in lines:
            while line:
                for i in range(len(line), 0, -1):
                    if self.canv.stringWidth(line[:i], "Courier", self.font_size) <= self.width:
                        self.wrapped_lines.append(line[:i])
                        line = line[i:]
                        break
        self.height = len(self.wrapped_lines) * self.line_height
        return (availWidth, self.height)

    def drawOn(self, canvas, x, y, _sW=0):
        canvas.saveState()
        y = y + self.height - self.line_height
        for line in self.wrapped_lines:
            if y < 0:  # If we've gone below the bottom margin, stop drawing
                break
            canvas.setFont("Courier", self.font_size)
            canvas.drawString(x, y, line)
            y -= self.line_height
        canvas.restoreState()

    def split(self, availWidth, availHeight):
        if availHeight < self.line_height:
            return []
        max_lines = int(availHeight / self.line_height)
        split1 = WrappedCode('\n'.join(self.wrapped_lines[:max_lines]))
        split2 = WrappedCode('\n'.join(self.wrapped_lines[max_lines:]))
        return [split1, split2]


def create_pdf(project_overview, toc, file_contents, output_path):
    doc = SimpleDocTemplate(str(output_path), pagesize=letter,
                            leftMargin=0.5*inch, rightMargin=0.5*inch,
                            topMargin=0.5*inch, bottomMargin=0.5*inch)
    styles = get_styles()
    flowables = []

    # Add project overview
    flowables.append(Paragraph("Project Overview", styles['Heading1']))
    flowables.append(Paragraph(project_overview, styles['Normal']))
    flowables.append(Spacer(1, 12))

    # Add table of contents
    flowables.append(Paragraph("Table of Contents", styles['Heading1']))
    flowables.append(Paragraph(toc, styles['Normal']))
    flowables.append(Spacer(1, 12))

    # Add file contents
    for i, (file_info, content) in enumerate(file_contents):
        if i > 0:
            flowables.append(PageBreak())
        flowables.append(Paragraph(file_info['path'], styles['Heading2']))
        flowables.append(
            Paragraph(f"Size: {file_info['size']} bytes", styles['Normal']))
        flowables.append(
            Paragraph(f"Created: {file_info['created']}", styles['Normal']))
        flowables.append(
            Paragraph(f"Modified: {file_info['modified']}", styles['Normal']))
        flowables.append(Spacer(1, 12))

        # Use the custom WrappedCode flowable for code content
        flowables.append(WrappedCode(content))

    doc.build(flowables)
