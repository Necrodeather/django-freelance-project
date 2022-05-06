from core.celery import app


@app.task
def start_parser_task():
    import asyncio
    from .services import parsing

    loop = asyncio.new_event_loop() 
    loop.run_until_complete(parsing.main())