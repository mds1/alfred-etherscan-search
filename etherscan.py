#!/usr/bin/python
# encoding: utf-8

import sys

# Workflow3 supports Alfred 3's new features. The `Workflow` class
# is also compatible with Alfred 2.
from workflow import Workflow3, ICON_WARNING, ICON_INFO

log = Workflow3.logger


def main(wf):
    log.debug("Execution started")
    # The Workflow3 instance will be passed to the function
    # you call from `Workflow3.run`.
    # Not super useful, as the `wf` object created in
    # the `if __name__ ...` clause below is global...
    #
    # Your imports go here if you want to catch import errors, which
    # is not a bad idea, or if the modules/packages are in a directory
    # added via `Workflow3(libraries=...)`
    import string

    # Get args from Workflow3, already in normalized Unicode.
    # This is also necessary for "magic" arguments to work.
    args = wf.args

    # Do stuff here ...
    # this is the address/keyword input by the user
    query = sys.argv[1].lower()
    log.debug("Query: " + query)

    # Set defaults
    title = "No results found"
    icon = ICON_WARNING
    url = False

    if query == "d" or query == "da" or query == "dai":
        title = "View Dai on Etherscan"
        icon = "img/dai.png"
        url = "https://etherscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F"

    elif query == "ch" or query == "cha" or query == "chai":
        title = "View Chai on Etherscan"
        icon = "img/chai.png"
        url = "https://etherscan.io/token/0x06AF07097C9Eeb7fD685c692751D5C66dB49c215"

    elif query == "s" or query == "sa" or query == "sai":
        title = "View Sai on Etherscan"
        icon = "img/sai.png"
        url = "https://etherscan.io/token/0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359"

    elif query == "u" or query == "us" or query == "usd" or query == "usdc":
        title = "View USD Coin on Etherscan"
        icon = "img/usdc.png"
        url = "https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"

    elif (
        query == "m"
        or query == "ma"
        or query == "mak"
        or query == "make"
        or query == "maker"
        or query == "mkr"
    ):
        title = "View Maker on Etherscan"
        icon = "img/maker.png"
        url = "https://etherscan.io/token/0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2"

    elif query == "cd" or query == "cda" or query == "cdai":
        title = "View cDAI on Etherscan"
        icon = "img/cdai.png"
        url = "https://etherscan.io/token/0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643"

    elif query == "cs" or query == "csa" or query == "csai":
        title = "View cSAI on Etherscan"
        icon = "img/csai.png"
        url = "https://etherscan.io/token/0xf5dce57282a584d2746faf1593d3121fcac444dc"

    elif query == "cu" or query == "cus" or query == "cusd" or query == "cusdc":
        title = "View cUSDC on Etherscan"
        icon = "img/cusdc.png"
        url = "https://etherscan.io/token/0x39aa39c021dfbae8fac545936693ac917d5e7563"

    elif query == "ce" or query == "cet" or query == "ceth":
        title = "View cETH on Etherscan"
        icon = "img/ceth.png"
        url = "https://etherscan.io/token/0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5"

    elif (
        query == "usdt"
        or query == "t"
        or query == "te"
        or query == "tet"
        or query == "teth"
        or query == "tethe"
        or query == "tether"
    ):
        title = "View Tether on Etherscan"
        icon = "img/tether.png"
        url = "https://etherscan.io/token/0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5"

    elif query[-4:] == ".eth":
        title = "View ENS address '" + query + "'"
        icon = "img/ens.png"
        url = "https://etherscan.io/enslookup?q=" + query

    elif len(query) == 66 or len(query) == 64:
        title = "View transaction '" + query + "'"
        icon = "icon.png"
        url = "https://etherscan.io/tx/" + query

    elif len(query) == 42 or len(query) == 40:
        title = "View address '" + query + "'"
        icon = "icon.png"
        url = "https://etherscan.io/address/" + query

    else:
        # If alphanumeric, append .eth and use ENS
        if query.isalnum():
            title = "View ENS address '" + query + ".eth" + "'"
            icon = "img/ens.png"
            url = "https://etherscan.io/enslookup-search?search=" + query + ".eth"

        # if query contains periods
        if "." in query:
            splitQuery = filter(None, query.split("."))
            ensPrefix = ".".join(splitQuery)
            ensDomain = ensPrefix + ".eth"
            title = "View ENS address '" + ensDomain
            icon = "img/ens.png"
            url = "https://etherscan.io/enslookup-search?search=" + ensDomain

    # Add an item to Alfred feedback
    wf.add_item(
        title=title,
        icon=icon,
        arg=url,  # argument to pass to Alfred
        valid=not not url,  # tells Alfred item is actionable
    )

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but subsequent calls
    # are ignored (otherwise the JSON sent to Alfred would be invalid).
    wf.send_feedback()


if __name__ == "__main__":
    # Create a global `Workflow3` object
    wf = Workflow3(update_settings={
                   "github_slug": "mds1/alfred-etherscan-search"})
    log = wf.logger

    # Check for updates
    # http://www.deanishe.net/alfred-workflow/guide/update.html#guide-updates
    if wf.update_available:
        wf.add_item('New version available',
                    'Action this item to install the update',
                    autocomplete='workflow:update',
                    icon=ICON_INFO)

    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))
