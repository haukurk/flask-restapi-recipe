__author__ = 'haukurk'

from optparse import OptionParser, OptionGroup
from restapi.utils.validation import is_valid_ipv4
from restapi.components.auth.controllers import show_all_keys, generate_key, show_key, delete_key


usage = "usage: %prog [options] arg"
parser = OptionParser(usage)

group_auth = OptionGroup(parser, "Authentication Options",
                         "Caution: if you remove keys they are not unrecoverable.")

group_auth.add_option("-g", "--generate",
                      help="Generate API key for an IP address",
                      action="store", type="string", dest="generate")
group_auth.add_option("-c", "--comment",
                      help="Comment for generated entry (OPTIONAL)",
                      action="store", type="string", dest="comment")
group_auth.add_option("-d", "--delete",
                      help="Delete API key identified by API ID",
                      action="store", type="string", dest="delete")
group_auth.add_option("-a", "--showall",
                      help="Show all authorized API keys",
                      action="store_true", dest="showall")

parser.add_option_group(group_auth)

(options, args) = parser.parse_args()

if options.showall:
    show_all_keys()

elif options.generate:
    if is_valid_ipv4(options.generate) is True:
        if options.comment is None:
            generate_key(options.generate, "N/A")
        else:
            generate_key(options.generate, options.comment)
    else:
        print("Please provide a correct IP address")

elif options.delete:
    delete_key(options.delete)

else:
    parser.print_help()