##
##

from __future__ import print_function

import baseBufrMosTestCase
import unittest

#
# Test DAF support for bufrmosAVN data
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/16        4795          mapeters       Initial Creation.
#    04/11/16        5548          tgurney        Cleanup
#    04/18/16        5548          tgurney        More cleanup
#
#


class BufrMosAvnTestCase(baseBufrMosTestCase.BufrMosTestCase):
    """Test DAF support for bufrmosAVN data"""

    datatype = "bufrmosAVN"

    # All tests inherited from superclass
