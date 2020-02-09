# Alfred Etherscan Search

Alfred workflow to quickly search addresses, transactions, and ENS Domains on Etherscan

- [Alfred Etherscan Search](#alfred-etherscan-search)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)


## Installation

1. Download the `.alfredworkflow` file from the
[GitHub releases](https://github.com/mds1/alfred-etherscan-search/releases/latest) page
2. Double-click the file to install

## Usage

The default keyword is `es`, but this can be changed if desired. Examples usage:

| Command                | Description                                                                                                                                                                                       |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `es <address>`         | Opens the provided address on Etherscan.                                                                                                                                                          |
| `es <transactionHash>` | Opens the provided transaction hash on Etherscan.                                                                                                                                                 |
| `es <ensDomain>`       | Opens the provided ENS domain on Etherscan.<br>Supports subdomains, and the `.eth` suffix<br>will be added automatically if not provided.                                                         |
| `es <tokenName>`       | Opens the provided token on Etherscan. Supported<br>values for `tokenName` include `dai`, `chai`, `sai`,<br>`usdc`, `usdt` or `tether`, `mkr` or `maker`, `cdai`,<br>`csai`, `cusdc`, and `ceth`. |

## License

This workflow is released under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements

This project utilizes the
[alfred-workflow](https://github.com/deanishe/alfred-workflow)
tool built by [@deanishe](https://github.com/deanishe)
