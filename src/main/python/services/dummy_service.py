import asyncio
import time

from notification_sender import Notification
from runner import Filter
from services.abstract_service import AbstractService


class DummyService(AbstractService):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, *kwargs)
        with self.METRICS_INIT_TIME.time():
            time.sleep(2)

    def get_candidate_native_id(self, candidate) -> str:
        # candidate entity id extractor
        return super().get_candidate_native_id(candidate)

    async def candidate_to_notification(self, c) -> Notification:
        # convert raw flat entity to a find_a_flat.notification_sender.Notification
        return await super().candidate_to_notification(c)

    # @AbstractService.RUN_TIME.time()
    async def run(self):
        self.bar()
        # Main entry point
        # White scraper here use self.push_candidate(candidate) passing a raw website flat entity
        return await asyncio.sleep(1)

    def bar(self):
        time.sleep(1)


if __name__ == '__main__':
    f = Filter(arrondissements=[75001, 75002, 75003], max_price=1300, min_area=25)
    service = DummyService(f, False)
    asyncio.get_event_loop().run_until_complete(service.run())
