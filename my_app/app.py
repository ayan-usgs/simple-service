import falcon

from .environment_getter import EnvironmentGetter


api = application = falcon.API()

eg = EnvironmentGetter()

api.add_route('/env_getter/', eg)
