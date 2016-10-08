===========
Odoo Sentry
===========

Odoo module which allows painless Sentry_ integration with Odoo.

Supported Odoo versions: 8.0, 9.0

Installation
------------

The module can be installed just like any other Odoo module, by adding the
module's parent directory to Odoo *addons_path*.


This module requires the raven_ Python package. It can be installed using pip::

    pip install raven

Configuration
-------------

The following additional configuration options can be added to your Odoo
configuration file:

==========================  ====================================================================  ==================
        Option                                          Description                                     Default
==========================  ====================================================================  ==================
sentry_dsn                  Sentry *Data Source Name*. You can find this value in your Sentry     *''*
                            project configuration. Typically it looks something like this:
                            *https://<public_key>:<secret_key>@sentry.example.com/<project id>*
                            This is the only required option in order to use the module.

sentry_enabled              Whether or not Sentry logging is enabled.                             *True*

sentry_report_user_errors   Whether user errors should also be reported to Sentry. These          *False*
                            include:

                            * *except_orm*:
                                * *UserError*
                                * *ValidationError*
                                * *AccessError*
                                * *MissingError*
                            * *AccessDenied*
                            * *Warning*
                            * *RedirectWarning*
                            * *osv.except_osv* (legacy)

sentry_include_context      If enabled, additional context data will be extracted from current    *True*
                            HTTP request and user session (if available). This has no effect
                            for Cron jobs, as no request/session is available inside a Cron job.

sentry_logging_level        The minimal logging level for which to send reports to Sentry.        *warn*
                            Possible values: *notset*, *debug*, *info*, *warn*, *error*,
                            *critical*. It is recommended to have this set to at least *warn*,
                            to avoid spamming yourself with Sentry events.

sentry_environment          Environment, in which Odoo is running, eg. *staging*, *production*.

sentry_auto_log_stacks      Whether Raven automatically log frame stacks (including locals) for   *False*
                            all calls as it would for exceptions.

sentry_odoo_dir             Absolute path to your Odoo installation directory. This is optional
                            and will only be used to extract the Odoo Git commit, which will be
                            sent to Sentry, to allow to distinguish between Odoo updates.
==========================  ====================================================================  ==================

Example Odoo configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~
Below is an example of Odoo configuration file with *Odoo Sentry* options::

    [options]
    sentry_client_dsn = https://<public_key>:<secret_key>@sentry.example.com/<project id>
    sentry_enabled = true
    sentry_report_user_errors = true
    sentry_include_context = true
    sentry_logging_level = warn
    sentry_environment = production
    sentry_auto_log_stacks = false
    sentry_odoo_dir = /home/odoo/odoo/

History
-------

This module was originally written by `Mohammed Barsi`_.
In version 2.0.0 it was rewritten from scratch by HBEE_.

Known issues
------------

No database separation
~~~~~~~~~~~~~~~~~~~~~~

*Odoo Sentry* module functions by intercepting all Odoo logging records. This
means that once installed in one database, it will intercept and report errors
for all Odoo databases, which are used on that Odoo server.


.. _Sentry: https://sentry.io/
.. _Mohammed Barsi: https://github.com/barsi/
.. _HBEE: https://github.com/HBEE/
.. _raven: https://github.com/getsentry/raven-python
