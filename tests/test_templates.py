from src.notifications.templates import JobTemplate


def test_template():

    rows = [
        {
            "company": "Google",
            "title": "Principal SDET",
            "score": 90,
            "url": "test"
        }
    ]

    text = JobTemplate.top_jobs(rows)

    assert "Google" in text
    assert "Principal SDET" in text