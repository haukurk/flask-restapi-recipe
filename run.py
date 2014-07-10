__author__ = 'haukurk'

import code
from optparse import OptionParser, OptionGroup

usage = "usage: %prog [options] arg"
parser = OptionParser(usage)

group_ops = OptionGroup(parser, "Operational Options",
                        "Run a development server or a debugging shell.")

group_ops.add_option("-r", "--run",
                     help="Run API (Developement Server)",
                     action="store_true", dest="run")
group_ops.add_option("-z", "--shell",
                     help="Run shell",
                     action="store_true", dest="shell")
group_ops.add_option("-i", "--init",
                     help="Initialize the application (first use)",
                     action="store_true", dest="init")

parser.add_option_group(group_ops)

(options, args) = parser.parse_args()

if options.run is True:
    from restapi import app, db
    print("Starting the Development HTTP server..")
    app.run(debug=True, host="0.0.0.0")

elif options.init is True:
    from restapi import app, db
    print("Creating database..")
    db.create_all()

elif options.shell:
    from restapi import app, db
    with app.app_context():
        code.interact(local={
            "app": app,
            "db": db
        })

else:
    parser.print_help()