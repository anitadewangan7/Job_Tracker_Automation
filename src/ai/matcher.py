from src.ai.cache import AICache
from src.ai.cost_tracker import (
    CostTracker
)
from src.ai.parser import (
    AIResponseParser
)
from src.ai.prompt_builder import (
    PromptBuilder
)


class AIMatcher:

    def __init__(
        self,
        provider
    ):

        self.provider = provider

    def match(
        self,
        resume,
        job
    ):

        cache_key = (
            AICache.hash_text(
                job.description
            )
        )

        cached = (
            AICache.get(cache_key)
        )

        if cached:
            return cached

        prompt = (
            PromptBuilder.build(
                resume,
                job.description
            )
        )

        response = (
            self.provider.generate(
                prompt
            )
        )

        result = (
            AIResponseParser.parse(
                response
            )
        )

        AICache.set(
            cache_key,
            result
        )

        CostTracker.increment()

        return result