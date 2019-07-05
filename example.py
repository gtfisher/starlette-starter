from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.staticfiles import StaticFiles


app = Starlette()
app.debug = True
app.mount('/static', StaticFiles(directory="static"))


@app.route('/hello')
def homepage(request):
    return PlainTextResponse('Hello, world!')

@app.route('/user/me')
def user_me(request):
    username = "John Doe"
    return PlainTextResponse('Hello, %s!' % username)

@app.route('/user/{username}')
def user(request):
    username = request.path_params['username']
    return PlainTextResponse('Hello, %s!' % username)


@app.websocket_route('/ws')
async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_text('Hello, websocket!')
    await websocket.close()


@app.on_event('startup')
def startup():
    print('Ready to go')