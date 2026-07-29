from django.core.management.base import BaseCommand
from apps.team.models import TeamMember


class Command(BaseCommand):
    help = "Load initial team members"

    def handle(self, *args, **kwargs):

        members = [
            {
                "name": "William (Bill) E. Harrell, Jr.",
                "role_title": "Founder & Orthodontist",
                "credentials": "DMD",
                "specialty": "Board-Certified Orthodontist (ABO); Certified in Dental Sleep Medicine",
                "is_doctor": True,
                "is_published": True,

                "bio": """Dr. Harrell is married to Joyce (Jay) Harrell, who is the director of the Infant/Toddler department at Jacob's Ladder. They have two children, including Tatum Harrell.

Dr. William (Bill) Harrell is originally from Columbus, GA. He graduated from the University of Alabama in Tuscaloosa with a double major in Chemistry and Math and a minor in Biology, then graduated from the UAB School of Dentistry in Birmingham in 1975 with his Doctor of Dental Medicine (DMD). He completed his orthodontic residency at the University of Pennsylvania School of Dental Medicine in Philadelphia in 1977.

He is in private orthodontic practice in Alexander City, Alabama and Auburn/Opelika, Alabama, and is a Board-Certified Orthodontist (ABO). Dr. Harrell is the first orthodontic private practice in Alabama to have ConeBeam CT (CBCT) and the first in the USA to combine both ConeBeam CT (CBCT) and 3D facial imaging.

Dr. Harrell is presently writing and will be the lead Editor of a textbook, "Growing into Breathing Problems: The Quest for Collaborative Lifetime Solutions" (note: the client's Publications section names this same in-press Springer book as "Sleep, Craniofacial Form, and Airway Function Disorders" -- both titles appear in the client's own materials; please confirm the final title).

Teaching: Dr. Harrell is a Professor at the University of Alabama at Birmingham, Orthodontic Department, where he teaches and lectures on Cone Beam CT imaging, airway, and TMJ disorders to doctors from all over the world. He publishes scientific articles, chapters, and books on these subjects.""",

                "education": """DMD -- University of Alabama at Birmingham School of Dentistry (1975)
Orthodontic Residency -- University of Pennsylvania School of Dental Medicine (1977)
BS, Chemistry & Math (minor Biology) -- University of Alabama, Tuscaloosa"""
            },

            {
                "name": "Tori",
                "role_title": "Staff",
                "credentials": "",
                "specialty": "",
                "bio": "",
                "education": "",
                "is_doctor": False,
                "is_published": True,
            },

            {
                "name": "Jessica",
                "role_title": "Staff",
                "credentials": "",
                "specialty": "",
                "bio": "",
                "education": "",
                "is_doctor": False,
                "is_published": True,
            },

            {
                "name": "Haley",
                "role_title": "Staff",
                "credentials": "",
                "specialty": "",
                "bio": "",
                "education": "",
                "is_doctor": False,
                "is_published": True,
            },

            {
                "name": "Bill III",
                "role_title": "Staff",
                "credentials": "",
                "specialty": "",
                "bio": "",
                "education": "",
                "is_doctor": False,
                "is_published": True,
            },
        ]

        for member in members:
            TeamMember.objects.update_or_create(
                name=member["name"],
                defaults=member
            )

        self.stdout.write(
            self.style.SUCCESS("Team members loaded successfully")
        )