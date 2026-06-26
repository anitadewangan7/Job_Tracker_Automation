class DuplicateFilter:

    @staticmethod
    def remove_duplicates(jobs):

        seen = set()

        result = []

        for job in jobs:

            key = (
                job.company.lower(),
                job.title.lower()
            )

            if key not in seen:

                seen.add(key)

                result.append(job)

        return result