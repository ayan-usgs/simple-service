import json
import os

import falcon


class EnvironmentGetter:

    def on_get(self, req, resp):
        env_var = req.params['variable']
        env_var_result = os.getenv(env_var)
        resp.body = json.dumps({env_var: env_var_result})
        resp.status = falcon.HTTP_200
