import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def organization_create(context, data_dict=None):
    # Get the user name of the logged-in user.
    user_name = context['user']

    # Get a list of the members of the 'org-mods' group.
    try:
        members = toolkit.get_action('member_list')(
            data_dict={'id': 'org-mods', 'object_type': 'user'})
    except toolkit.ObjectNotFound:
        # The org-mods group doesn't exist.
        return {'success': False,
                'msg': "The org-mods groups doesn't exist, so only sysadmins "
                       "are authorized to create organizations."}

    # 'members' is a list of (user_id, object_type, capacity) tuples, we're
    # only interested in the user_ids.
    member_ids = [member_tuple[0] for member_tuple in members]

    # We have the logged-in user's user name, get their user id.
    convert_user_name_or_id_to_id = toolkit.get_converter(
        'convert_user_name_or_id_to_id')
    try:
        user_id = convert_user_name_or_id_to_id(user_name, context)
    except toolkit.Invalid:
        # The user doesn't exist (e.g. they're not logged-in).
        return {'success': False,
                'msg': 'You must be logged-in as a member of the org-mods '
                       'group to create new organizations.'}

    # Finally, we can test whether the user is a member of the org-mods group.
    if user_id in member_ids:
        return {'success': True}
    else:
        return {'success': False,
                'msg': 'Only org-mods are allowed to create organizations'}

class OrgauthPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthFunctions)
    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'orgAuth')

    def get_auth_functions(self):
        return {'organization_create' : organization_create}