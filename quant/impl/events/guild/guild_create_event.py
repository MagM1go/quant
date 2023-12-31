from quant.impl.events.event import Event
from quant.entities.guild import Guild
from quant.impl.events.types import EventTypes
from quant.utils.cache.cache_manager import CacheManager


class GuildCreateEvent(Event):
    API_EVENT_NAME: EventTypes = EventTypes.GUILD_CREATE

    guild: Guild

    def process_event(self, cache_manager: CacheManager, **kwargs):
        self.guild = Guild(**kwargs)

        cache_manager.add_guild(self.guild)

        return self
