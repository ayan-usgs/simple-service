import falcon

from .environment_getter import EnvironmentGetter, EvenOdd, StringLength


api = application = falcon.API()

eg = EnvironmentGetter()
eo = EvenOdd()
sl = StringLength()

api.add_route('/env-getter/', eg)
api.add_route('/integer/', eo)
api.add_route('/string-length/', sl)
