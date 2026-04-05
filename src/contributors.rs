pub struct ContributorInfo {
    pub name: &'static str,
    pub email: &'static str,
}

pub struct ContributorGroup {
    pub name: &'static str,
    pub contributors: &'static [ContributorInfo],
}

pub static SWIFT_CONTRIBUTORS_CORE: &[ContributorInfo] = &[ContributorInfo {
    name: "Kamil Machowski",
    email: "machowskikamil@proton.me",
}];
/*
pub static SWIFT_CONTRIBUTORS_ACTIVE: &[ContributorInfo] = &[];
pub static SWIFT_CONTRIBUTORS_SERVER: &[ContributorInfo] = &[];
pub static SWIFT_CONTRIBUTORS_TRANSLATORS_SUPERVISION: &[ContributorInfo] = &[];
pub static SWIFT_CONTRIBUTORS_DOCUMENTATION_SUPERVISION: &[ContributorInfo] = &[];
pub static SWIFT_CONTRIBUTORS_PREVIOUS: &[ContributorInfo] = &[];
*/

pub static SWIFT_CONTRIBUTORS: &[ContributorGroup] = &[
    ContributorGroup {
        name: "Core developers",
        contributors: SWIFT_CONTRIBUTORS_CORE,
    }, /*ContributorGroup {
           name: "Active contributors",
           contributors: SWIFT_CONTRIBUTORS_ACTIVE,
       },
       ContributorGroup {
           name: "Servers maintained by",
           contributors: SWIFT_CONTRIBUTORS_SERVER,
       },
       ContributorGroup {
           name: "Translations supervision",
           contributors: SWIFT_CONTRIBUTORS_TRANSLATORS_SUPERVISION,
       },
       ContributorGroup {
           name: "Documentation supervision",
           contributors: SWIFT_CONTRIBUTORS_DOCUMENTATION_SUPERVISION,
       },
       ContributorGroup {
           name: "Previous contributors",
           contributors: SWIFT_CONTRIBUTORS_PREVIOUS,
       },*/
];
