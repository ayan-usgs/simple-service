import falcon

from .services import EnvironmentGetter, EvenOdd, StringLength


api = application = falcon.API()

eg = EnvironmentGetter()
eo = EvenOdd()
sl = StringLength()

api.add_route('/py-app/env-getter/', eg)
api.add_route('/py-app/integer/', eo)
api.add_route('/py-app/string-length/', sl)
