import random
from scrapy.exceptions import IgnoreRequest


class ZyteAPIErrorMiddleware:

    RETRY_HTTP_CODES = [429, 500, 503, 520, 521]

    def process_response(self, request, response, spider):

        status = response.status

        if status in self.RETRY_HTTP_CODES:

            retry_times = request.meta.get("retry_times", 0) + 1
            max_retry = 5

            if retry_times <= max_retry:

                spider.logger.warning(
                    f"Retry {retry_times} for {request.url} status={status}"
                )

                new_request = request.copy()
                new_request.meta["retry_times"] = retry_times
                new_request.dont_filter = True

                return new_request

            spider.logger.error(
                f"Max retries exceeded for {request.url}"
            )

        if status in [400, 401, 422]:

            spider.logger.error(
                f"Invalid request {status} for {request.url}"
            )

        if status == 403:
            spider.logger.error(
                "Zyte account suspended or limit reached"
            )
            raise IgnoreRequest()

        return response