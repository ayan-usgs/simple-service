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


class EvenOdd:

    def on_get(self, req, resp):
        number_val = req.params.get('value')
        if number_val is None:
            result = None
        else:
            modulo_val = float(number_val) % 2
            if modulo_val == 0:
                result = True
            else:
                result = False
        resp.body = json.dumps({'isEven': result})
        resp.status = falcon.HTTP_200


class StringLength:

    def on_get(self, req, resp):
        some_str = req.params.get('string', '')
        resp.body = json.dumps({'stringLength': len(some_str)})
        resp.status = falcon.HTTP_200
