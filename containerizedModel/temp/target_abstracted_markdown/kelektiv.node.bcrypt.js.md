# node.bcrypt.js

@abstr_hyperlink @abstr_hyperlink 

A library to help you hash passwords.

You can read about @abstr_hyperlink as well as in the following article: @abstr_hyperlink 

## If You Are Submitting Bugs or Issues

Verify that the node version you are using is a _stable_ version; it has an even major release number. Unstable versions are currently not supported and issues created while using an unstable version will be closed.

If you are on a stable version of node, please provide a sufficient code snippet or log files for installation issues. The code snippet does not require you to include confidential information. However, it must provide enough information such that the problem can be replicable. Issues which are closed without resolution often lack required information for replication.

## Version Compatibility

| Node Version | Bcrypt Version | | -------------- | -------------- | | @abstr_number . @abstr_number | <= @abstr_number . @abstr_number | | @abstr_number . @abstr_number , @abstr_number . @abstr_number , @abstr_number . @abstr_number | >= @abstr_number . @abstr_number | | @abstr_number . @abstr_number | >= @abstr_number . @abstr_number | | @abstr_number | <= @abstr_number . @abstr_number . @abstr_number | | @abstr_number | >= @abstr_number . @abstr_number . @abstr_number | | @abstr_number , @abstr_number | >= @abstr_number | | @abstr_number (nightly) | >= @abstr_number . @abstr_number . @abstr_number |

`node-gyp` only works with stable/released versions of node. Since the `bcrypt` module uses `node-gyp` to build and install, you'll need a stable version of node to use bcrypt. If you do not, you'll likely see an error that starts with:

@abstr_code_section 

## Security Issues And Concerns

> Per bcrypt implementation, only the first @abstr_number characters of a string are used. Any extra characters are ignored when matching passwords.

As should be the case with any security tool, this library should be scrutinized by anyone using it. If you find or suspect an issue with the code, please bring it to my attention and I'll spend some time trying to make sure that this tool is as secure as possible.

To make it easier for people using this tool to analyze what has been surveyed, here is a list of BCrypt related security issues/concerns as they've come up.

  * An @abstr_hyperlink was found with a version of the Blowfish algorithm developed for John the Ripper. This is not present in the OpenBSD version and is thus not a problem for this module. HT @abstr_hyperlink .



## Compatibility Note

This library supports `$ @abstr_number a$` and `$ @abstr_number b$` prefix bcrypt hashes. `$ @abstr_number x$` and `$ @abstr_number y$` hashes are specific to bcrypt implementation developed for Jon the Ripper. In theory, they should be compatible with `$ @abstr_number b$` prefix.

Compatibility with hashes generated by other languages is not @abstr_number % guaranteed due to difference in character encodings. However, it should not be an issue for most cases.

### Migrating from v @abstr_number . @abstr_number .x

Hashes generated in earlier version of `bcrypt` remain @abstr_number % supported in `v @abstr_number .x.x` and later versions. In most cases, the migration should be a bump in the `package.json`.

Hashes generated in `v @abstr_number .x.x` using the defaults parameters will not work in earlier versions.

## Dependencies

  * NodeJS
  * `node-gyp`
    * Please check the dependencies for this tool at: https://github.com/nodejs/node-gyp
    * Windows users will need the options for c# and c++ installed with their visual studio instance.
    * Python @abstr_number .x
  * `OpenSSL` \- This is only required to build the `bcrypt` project if you are using versions <= @abstr_number . @abstr_number . @abstr_number . Otherwise, we're using the builtin node crypto bindings for seed data (which use the same OpenSSL code paths we were, but don't have the external dependency).



## Install via NPM

@abstr_code_section **_Note:_** OS X users using Xcode @abstr_number . @abstr_number . @abstr_number or above may need to run the following command in their terminal prior to installing if errors occur regarding xcodebuild: `sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer`

_Pre-built binaries for various NodeJS versions are made available on a best-effort basis._

Only the current stable and supported LTS releases are actively tested against. Please note that there may be an interval between the release of the module and the availabilty of the compiled modules.

Currently, we have pre-built binaries that support the following platforms:

@abstr_number . Windows x @abstr_number and x @abstr_number @abstr_number . Linux x @abstr_number (GlibC targets only). Pre-built binaries for MUSL targets such as Apline Linux are not available. @abstr_number . macOS

If you face an error like this:

@abstr_code_section 

make sure you have the appropriate dependencies installed and configured for your platform. You can find installation instructions for the dependencies for some common platforms @abstr_hyperlink .

## Usage

### async (recommended)

@abstr_code_section 

#### To hash a password:

Technique @abstr_number (generate a salt and hash on separate function calls):

@abstr_code_section 

Technique @abstr_number (auto-gen a salt and hash):

@abstr_code_section 

Note that both techniques achieve the same end-result.

#### To check a password:

@abstr_code_section 

The "compare" function counters timing attacks (using a so-called 'constant-time' algorithm). In general, don't use the normal JavaScript string comparison functions to compare passwords, cryptographic keys, or cryptographic hashes if they are relevant to security.

### with promises

bcrypt uses whatever Promise implementation is available in `global.Promise`. NodeJS >= @abstr_number . @abstr_number has a native Promise implementation built in. However, this should work in any Promises/A+ compliant implementation.

Async methods that accept a callback, return a `Promise` when callback is not specified if Promise support is available.

@abstr_code_section @abstr_code_section 

This is also compatible with `async/await`

@abstr_code_section 

### sync

@abstr_code_section 

#### To hash a password:

Technique @abstr_number (generate a salt and hash on separate function calls):

@abstr_code_section 

Technique @abstr_number (auto-gen a salt and hash):

@abstr_code_section 

As with async, both techniques achieve the same end-result.

#### To check a password:

@abstr_code_section The "compareSync" function counters timing attacks (using a so-called 'constant-time' algorithm). In general, don't use the normal JavaScript string comparison functions to compare passwords, cryptographic keys, or cryptographic hashes if they are relevant to security.

### Why is async mode recommended over sync mode?

If you are using bcrypt on a simple script, using the sync mode is perfectly fine. However, if you are using bcrypt on a server, the async mode is recommended. This is because the hashing done by bcrypt is CPU intensive, so the sync version will block the event loop and prevent your application from servicing any other inbound requests or events. The async version uses a thread pool which does not block the main event loop.

## API

`BCrypt.`

  * `genSaltSync(rounds, minor)`
    * `rounds` \- [OPTIONAL] - the cost of processing the data. (default - @abstr_number )
    * `minor` \- [OPTIONAL] - minor version of bcrypt to use. (default - b)
  * `genSalt(rounds, minor, cb)`
    * `rounds` \- [OPTIONAL] - the cost of processing the data. (default - @abstr_number )
    * `minor` \- [OPTIONAL] - minor version of bcrypt to use. (default - b)
    * `cb` \- [OPTIONAL] - a callback to be fired once the salt has been generated. uses eio making it asynchronous. If `cb` is not specified, a `Promise` is returned if Promise support is available. 
      * `err` \- First parameter to the callback detailing any errors.
      * `salt` \- Second parameter to the callback providing the generated salt.
  * `hashSync(data, salt)`
    * `data` \- [REQUIRED] - the data to be encrypted.
    * `salt` \- [REQUIRED] - the salt to be used to hash the password. if specified as a number then a salt will be generated with the specified number of rounds and used (see example under **Usage** ).
  * `hash(data, salt, cb)`
    * `data` \- [REQUIRED] - the data to be encrypted.
    * `salt` \- [REQUIRED] - the salt to be used to hash the password. if specified as a number then a salt will be generated with the specified number of rounds and used (see example under **Usage** ).
    * `cb` \- [OPTIONAL] - a callback to be fired once the data has been encrypted. uses eio making it asynchronous. If `cb` is not specified, a `Promise` is returned if Promise support is available. 
      * `err` \- First parameter to the callback detailing any errors.
      * `encrypted` \- Second parameter to the callback providing the encrypted form.
  * `compareSync(data, encrypted)`
    * `data` \- [REQUIRED] - data to compare.
    * `encrypted` \- [REQUIRED] - data to be compared to.
  * `compare(data, encrypted, cb)`
    * `data` \- [REQUIRED] - data to compare.
    * `encrypted` \- [REQUIRED] - data to be compared to.
    * `cb` \- [OPTIONAL] - a callback to be fired once the data has been compared. uses eio making it asynchronous. If `cb` is not specified, a `Promise` is returned if Promise support is available. 
      * `err` \- First parameter to the callback detailing any errors.
      * `same` \- Second parameter to the callback providing whether the data and encrypted forms match [true | false].
  * `getRounds(encrypted)` \- return the number of rounds used to encrypt a given hash 
    * `encrypted` \- [REQUIRED] - hash from which the number of rounds used should be extracted.



## A Note on Rounds

A note about the cost. When you are hashing your data the module will go through a series of rounds to give you a secure hash. The value you submit there is not just the number of rounds that the module will go through to hash your data. The module will use the value you enter and go through `@abstr_number ^rounds` iterations of processing.

From @garthk, on a @abstr_number GHz core you can roughly expect:
    
    
    rounds= @abstr_number  : ~ @abstr_number  hashes/sec
    rounds= @abstr_number  : ~ @abstr_number  hashes/sec
    rounds= @abstr_number : ~ @abstr_number  hashes/sec
    rounds= @abstr_number : ~ @abstr_number   hashes/sec
    rounds= @abstr_number :  @abstr_number - @abstr_number  hashes/sec
    rounds= @abstr_number : ~ @abstr_number  sec/hash
    rounds= @abstr_number : ~ @abstr_number . @abstr_number  sec/hash
    rounds= @abstr_number : ~ @abstr_number  sec/hash
    rounds= @abstr_number : ~ @abstr_number  hour/hash
    rounds= @abstr_number :  @abstr_number - @abstr_number  days/hash
    

## Hash Info

The characters that comprise the resultant hash are `./ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz @abstr_number $`.

Resultant hashes will be @abstr_number characters long.

## Testing

If you create a pull request, tests better pass :)

@abstr_code_section 

## Credits

The code for this comes from a few sources:

  * blowfish.cc - OpenBSD
  * bcrypt.cc - OpenBSD
  * bcrypt::gen_salt - @abstr_hyperlink 
  * bcrypt_node.cc - me



## Contributors

  * @abstr_hyperlink - Early MacOS X support (when we used libbsd)
  * @abstr_hyperlink - Fixes for thread safety with async calls
  * @abstr_hyperlink - Found a timing attack in the comparator
  * @abstr_hyperlink - Initial Cygwin support
  * @abstr_hyperlink - packaging fixes
  * @abstr_hyperlink - packaging fixes
  * @abstr_hyperlink - Testing around concurrency issues
  * @abstr_hyperlink - Documentation fixes
  * @abstr_hyperlink - Code refactoring, general rot reduction, compile options, better memory management with delete and new, and an upgrade to libuv over eio/ev.
  * @abstr_hyperlink - Code changes to support @abstr_number . @abstr_number . @abstr_number +
  * @abstr_hyperlink - Fixed a thread safety issue in nodejs that was perfectly mappable to this module.
  * @abstr_hyperlink - Bindings and build process.
  * @abstr_hyperlink - Windows Support
  * @abstr_hyperlink - Windows Support
  * @abstr_hyperlink - $ @abstr_number b$ hash support, ES @abstr_number Promise support



## License

Unless stated elsewhere, file headers or otherwise, the license as stated in the LICENSE file.
