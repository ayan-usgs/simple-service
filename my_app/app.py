import falcon

from .environment_getter import EnvironmentGetter, EvenOdd


api = application = falcon.API()

eg = EnvironmentGetter()
eo = EvenOdd()

api.add_route('/env_getter/', eg)
api.add_route('/integer/', eo)
