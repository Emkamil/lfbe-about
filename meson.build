project('swift-about', 'rust', version: '1.0.2')

i18n = import('i18n')
install_data(
    sources: ['data/licenses/gpl-3.0.txt', 'data/licenses/lgpl-3.0.txt', 'data/licenses/bsd-3-clause.txt'],
    install_dir: get_option('datadir') / 'swift/licenses'
)

i18n.gettext('swift-about', preset: 'glib')
