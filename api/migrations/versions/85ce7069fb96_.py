"""empty message

Revision ID: 85ce7069fb96
Revises: 33e175de61ca
Create Date: 2020-01-30 16:56:57.500161

"""

# revision identifiers, used by Alembic.
revision = '85ce7069fb96'
down_revision = '33e175de61ca'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

from app.email_template.models import EmailTemplate


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    email_template = table(
        'email_template',
        column('id', sa.Integer()),
        column('key', sa.String(50)),
        column('event_id', sa.Integer()),
        column('template', sa.String())
    )

    op.bulk_insert(
        email_template,
        [
            {
                'id': 1,
                'key': 'application-not-submitted',
                'event_id': None,
                'template': """
Dear {title} {firstname} {lastname},
We noticed that you started applying to attend the {event} but have not completed and submitted your application. This is a final reminder that you have until {deadline} to submit your application in order to be considered. Please complete and submit your application if you would still like to attend this event.
We have noticed that some people were confused about the "check your answers" page and may not have clicked on the Submit button on this page. Please be aware that you must click on the Submit button to confirm your application. If you do not receive an email from us with a copy of your answers, your application will not be considered.
Kind Regards,
The {organisation_name} Team
"""
            },
            {
                'id': 2,
                'key': 'application-not-started',
                'event_id': None,
                'template': """
Dear {title} {firstname} {lastname},
WE HAVE NOT RECEIVED YOUR APPLICATION TO ATTEND {event}
We noticed that you have created a {system_name} account, but have not yet started an application to attend {event}.
If you think you have already filled in the form, you may have not clicked on the SUBMIT button on the final page. If this is the case, we DO NOT have your application and unfortunately you will have to re-do it. We sincerely apologise for any confusion and inconvenience in this regard.
This is a final reminder that you have until {deadline} to complete and submit your application.
Please ensure you have submitted your application before this date if you would still like to attend this event.
Kind Regards,
The {organisation_name} Team
"""
            },
            {
                'id': 3,
                'key': 'withdrawal',
                'event_id': None,
                'template': """Dear {title} {firstname} {lastname},
This email serves to confirm that you have withdrawn your application to attend the Deep Learning Indaba 2019. 
If this was a mistake, you may resubmit an application before the application deadline. If the deadline has past, please get in touch with us.
Kind Regards,
The {organisation_name} Team
"""
            },
            {
                'id': 4,
                'key':'confirmation-response',
                'event_id': None,
                'template': """Dear {title} {firstname} {lastname},

Thank you for applying to attend {event_description}. Your application is being reviewed by our committee and we will get back to you as soon as possible. Included below is a copy of your responses.


{question_answer_summary}


Kind Regards,
The {event_name} Team"""
            }
        ]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
