"""
Seeds the database with ONLY the real, client-provided content: Dr.
Harrell's real bio, the real financing lineup (Cherry first), the real
referral-provider directory, and known publications/patents.

This intentionally does NOT create fake staff, fake reviews, fake
patients, or fake video transcripts -- run this once against a fresh
database to replace the earlier demo/mock seed with the real practice
data. Re-running is safe (uses update_or_create).

    python manage.py seed_real_data
"""
from django.core.management.base import BaseCommand
from apps.team.models import TeamMember
from apps.financing.models import FinancingOption
from apps.publications.models import Publication
from apps.referrals.models import ExternalProvider


HARRELL_BIO = (
    "Dr. Harrell is originally from Columbus, GA. He graduated from the University of Alabama in "
    "Tuscaloosa with a double major in Chemistry and Math and a minor in Biology, then graduated from "
    "the UAB School of Dentistry in Birmingham in 1975 with his Doctor of Dental Medicine (DMD). He "
    "completed his orthodontic residency at the University of Pennsylvania School of Dental Medicine "
    "in Philadelphia in 1977.\n\n"
    "He is in private orthodontic practice in Alexander City, Alabama and Auburn/Opelika, Alabama, and "
    "is a Board-Certified Orthodontist (ABO) and Certified in Dental Sleep Medicine. He worked with the "
    "late TMJ pioneers Dr. Bill Farrar and Dr. Bill McCarty in Montgomery, AL. Dr. Harrell has served as "
    "Vice-President and President of the Alabama Association of Orthodontists; as Secretary-Treasurer, "
    "VP, and President of the 9th District Dental Society of Alabama; and on the Board of Trustees and "
    "House of Delegates of the Alabama Dental Association, as well as various committees of the American "
    "Association of Orthodontists.\n\n"
    "Dr. Harrell's practice was the first orthodontic private practice in Alabama with ConeBeam CT "
    "(CBCT), and the first in the USA to combine CBCT with 3D facial imaging (3dMD) in early 2005. He is "
    "Chairperson of the RadSite ConeBeam CT Standards Committee, which sets reimbursement standards for "
    "the insurance industry.\n\n"
    "Dr. Harrell is a Professor at the University of Alabama at Birmingham Orthodontic Department, where "
    "he teaches on Cone Beam CT imaging, airway, TMJ disorders, and nasal resistance testing to doctors "
    "from around the world, and publishes scientific articles, chapters, and books on these subjects. He "
    "is presently lead editor of a textbook on pediatric sleep disorders related to altered craniofacial "
    "growth, published by Springer, co-edited with Dr. David Gozal, MD and Dr. David McIntosh, MBBS, "
    "FRACS, PhD."
)

REFERRAL_PROVIDERS = [
    ("Dr. Christopher Hope, MD", "Sleep Physician", ""),
    ("Dr. Tony McLeod, MD", "ENT", ""),
    ("Dr. Bill Blythe, MD", "ENT (Styles / Whatley)", ""),
    ("Dr. Mike Koslin, DMD", "Oral Surgeon \u2014 TMJ, MMA", ""),
    ("Dr. Patrick Lewis, MD, DMD", "Oral Surgeon \u2014 MMA, Sleep", ""),
    ("Dr. Brittany Maten, DMD", "Periodontist", ""),
    ("Dr. TJ Fuqua", "Oral & Facial Surgery", "OFS Auburn"),
    ("Dr. Ken Zouhary", "Oral & Facial Surgery", "OFS Auburn"),
    ("Dr. Brannon Heape", "Oral & Facial Surgery", "OFS Auburn"),
    ("Dr. Chelsea Johnson", "Oral & Facial Surgery", "OFS Auburn"),
    ("Dr. Richard Baxter, DMD", "Pediatric Dentist \u2014 Tongue Tie Release", "Alabama Tongue Tie Center, Pelham, AL"),
    ("Renata Nehme, RDH, OMFT", "Myofunctional Therapy", "Savannah, GA"),
    ("Lauren Hughes, SLP, OMFT", "Myofunctional Therapy / Speech-Language Pathology", "Birmingham, AL"),
    ("Dr. Sally & Brooks Lamberth, DMD", "General Dentist", "Alexander City, AL"),
    ("Dr. Wendy Holder, DMD", "General Dentist", "Alexander City, AL"),
    ("Dr. James Leonard, DMD", "General Dentist", "Alexander City, AL"),
    ("Dr. Wiggins, DMD", "General Dentist", "Alexander City, AL"),
    ("Dr. George Hardy, DMD", "General Dentist", "Alexander City, AL"),
    ("Dr. Joni Price, DMD", "General Dentist", "Alexander City, AL"),
    ("Sarrell", "Dental Practice", "Alexander City, AL"),
    ("Dr. Jim Phillips, DMD", "General Dentist", "Auburn/Opelika, AL"),
    ("Dr. Stephanie Stephens", "General Dentist", "Auburn/Opelika, AL"),
    ("Dr. Jose Reynolds, DMD", "General Dentist", "Auburn/Opelika, AL"),
    ("Dr. Karen Davidson", "Colleague / Co-author", ""),
    ("Dr. David McIntosh", "Pediatric ENT", "Australia"),
    ("Dr. David Gozal, MD", "Sleep Medicine \u2014 Dean, Joan C. Edwards School of Medicine", "Marshall University"),
    ("Dr. Jerry Simmons, MD", "Sleep Medicine", ""),
    ("Dr. Steve Carstensen, DDS", "Dental Sleep Medicine", ""),
    ("Dr. Audrey Yoon, DDS", "Colleague / Co-author (C-GASP)", ""),
]


class Command(BaseCommand):
    help = "Seed the database with the real Harrell Orthodontics content (no placeholders)."

    def handle(self, *args, **options):
        doctor, _ = TeamMember.objects.update_or_create(
            name="William (Bill) E. Harrell, Jr.",
            defaults=dict(
                role_title="Founder & Orthodontist",
                credentials="DMD",
                specialty="Board-Certified Orthodontist (ABO); Certified in Dental Sleep Medicine",
                bio=HARRELL_BIO,
                education=(
                    "DMD \u2014 University of Alabama at Birmingham School of Dentistry (1975)\n"
                    "Orthodontic Residency \u2014 University of Pennsylvania School of Dental Medicine (1977)\n"
                    "BS, Chemistry & Math (minor Biology) \u2014 University of Alabama, Tuscaloosa"
                ),
                is_doctor=True,
                order=0,
                is_published=True,
            ),
        )
        self.stdout.write(self.style.SUCCESS(f"Team member: {doctor}"))

        financing_rows = [
            ("cherry", "Cherry", "Buy Now, Pay Later \u2014 monthly payments designed for you.",
             "https://pay.withcherry.com/harrell-orthodontics", True, 0),
            ("credit_cards", "Credit Cards", "", "", False, 1),
            ("hsa", "Health Savings Accounts (HSA)", "", "", False, 2),
            ("health_financing_direct", "Health Financing Direct", "", "", False, 3),
            ("carecredit", "CareCredit", "", "https://www.carecredit.com/go/RWH396/", False, 4),
        ]
        for kind, name, tagline, url, is_primary, order in financing_rows:
            obj, _ = FinancingOption.objects.update_or_create(
                kind=kind,
                defaults=dict(
                    display_name=name, tagline=tagline, learn_more_url=url,
                    is_primary=is_primary, order=order, is_active=True,
                ),
            )
            self.stdout.write(self.style.SUCCESS(f"Financing: {obj}"))

        pubs = [
            ("Pediatric sleep textbook (title unconfirmed with client)", Publication.Kind.BOOK,
             "William E. Harrell, Jr., DMD (Lead Editor); David Gozal, MD; David McIntosh, MBBS, FRACS, PhD", None),
            ("Book chapter \u2014 Jacobson (CBCT)", Publication.Kind.BOOK_CHAPTER, "William E. Harrell, Jr., DMD", None),
            ("Book chapter \u2014 Essentials in Orthodontics", Publication.Kind.BOOK_CHAPTER, "William E. Harrell, Jr., DMD", None),
            ("Patent \u2014 InvisaTMJ\u00A9 (Invisible aligner TMJ therapy)", Publication.Kind.PATENT, "William E. Harrell, Jr., DMD", None),
        ]
        for title, kind, authors, year in pubs:
            obj, _ = Publication.objects.update_or_create(
                title=title, defaults=dict(kind=kind, authors=authors, year=year)
            )
            self.stdout.write(self.style.SUCCESS(f"Publication: {obj}"))

        for name, specialty, location in REFERRAL_PROVIDERS:
            obj, _ = ExternalProvider.objects.update_or_create(
                name=name, defaults=dict(specialty=specialty, location=location)
            )
        self.stdout.write(self.style.SUCCESS(f"Referral directory: {len(REFERRAL_PROVIDERS)} providers"))

        self.stdout.write(self.style.WARNING(
            "NOT seeded (no real data provided yet): additional team/staff members, "
            "video files & real captions, patient reviews, dated lectures/events, "
            "downloadable form PDFs. See ASSET_AUDIT.md."
        ))
