#!/usr/bin/env python3
import os
import sys
import argparse


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        raise RuntimeError('It requires Python 3.')
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain', '-d', action="store", dest="domain",
                        default='demo', type=str, help="domain to be loaded")
    parser.add_argument('--port', '-p', action="store", dest="port",
                        default=8081, type=int, help="port to host application on")
    parser.add_argument('--dburi', action="store", dest="dburi",
                        default='mongodb://localhost', type=str, help="backend database (MongoDB) service uri")
    args = parser.parse_args()

    # Set Environment variables associated to domain and backend database (MongoDB)
    os.environ['domain'] = args.domain
    os.environ['dburi'] = args.dburi

    from webapp import create_app, socketio
    app = create_app(debug=True)
    socketio.run(app, host='0.0.0.0', port=args.port)
