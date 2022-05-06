import asyncio

import pathes.parsing as parsing


loop = asyncio.new_event_loop()

loop.run_until_complete(parsing.main())