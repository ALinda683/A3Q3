# Name: ALinda Kumar Mazumder
# NSID: ugj683
# Student no: 11342454
# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Question nodechain_tostring starter code

import node as n

def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty (None)
    Post_conditions:
        None
    Return: A string representation of the nodes.
        NOTE: THIS VERSION OF THE FUNCTION IS KNOWN TO BE BROKEN!!!
    """
    if node_chain is None:
        return 'EMPTY'

    # walk along the chain
    walker = node_chain
    result = '[ {} |'.format(str(walker.get_data()))

    while walker.get_next() is not None:
        walker = walker.get_next()
        value = walker.get_data()
        # represent the next with an arrow-like figure
        result += ' *-]-->[ {} |'.format(str(value))

    # at the end of the chain, use '/'
    result += ' / ]'
    return result