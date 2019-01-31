import os

import controller


app_port = int(os.environ.get('APP_PORT', '8080'))
controller.serve(app_port)
