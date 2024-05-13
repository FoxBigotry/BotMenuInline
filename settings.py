from pydantic_settings import BaseSettings, SettingsConfigDict


class Messages:
    HELP_MESSAGE = (f"Bot alive: <code>/ping</code>\n"
                    f"Delete message history: <code>/reset</code>\n"
                    'Upload questionnaire data: <code>/pass_q {"parameter": "value",}</code>\n'
                    # f"Generate weekly report: <code>/week</code>\n"
                    # f"Generate daily report: <code>/day</code>\n"
                    # f"Set time for daily ping: <code>/set_daily_time</code>\n"
                    # f"Create ban warning for user: <code>/ban</code>\n"
                    # f"Ban current user: <code>/ban_user</code>\n"
                    # f"Unban current user: <code>/unban</code>\n"
                    f"Change bot language: /language\n"
                    f"Set daily time for communication (HH:MM): <code>/set_daily_time</code>\n"
                    f"Fill your info: /miniapp\n"
                    f"Under development: /diet_plan\n")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    TG_KEY: str


settings = Settings()
system_messages = Messages()

__all__ = ["settings"]
