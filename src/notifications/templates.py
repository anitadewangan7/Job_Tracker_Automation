class JobTemplate:

    @staticmethod
    def top_jobs(rows):

        body = "Top QA/SDET Jobs\n\n"

        for row in rows:

            body += (
                f"{row['company']}\n"
                f"{row['title']}\n"
                f"Score: {row['score']}\n"
                f"{row['url']}\n\n"
            )

        return body