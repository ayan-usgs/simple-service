import json
import os

import falcon


class EnvironmentGetter:

    def on_get(self, req, resp):
        env_var = req.params.get('variable')
        if env_var is None:
            env_vars = os.environ.keys()
            resp.body = json.dumps({'variableCount': len(env_vars)})
        else:
            env_var_result = os.getenv(env_var)
            resp.body = json.dumps({env_var: env_var_result})
        resp.status = falcon.HTTP_200