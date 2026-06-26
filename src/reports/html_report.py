from jinja2 import Template


class HTMLReport:

    @staticmethod
    def generate(
        data,
        output_file="jobs.html"
    ):

        template = Template(
            """
            <html>
            <body>

            <h1>QA/SDET Job Report</h1>

            <table border="1">

            <tr>
                <th>Company</th>
                <th>Title</th>
                <th>Score</th>
            </tr>

            {% for row in rows %}

            <tr>

                <td>{{row.company}}</td>

                <td>{{row.title}}</td>

                <td>{{row.score}}</td>

            </tr>

            {% endfor %}

            </table>

            </body>
            </html>
            """
        )

        html = template.render(
            rows=data
        )

        with open(
            output_file,
            "w"
        ) as f:

            f.write(html)

        return output_file