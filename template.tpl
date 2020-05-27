Hi {{ data.gift_giver.first_name }},

Welcome to the Múinteoir Gift Exchange.  I am so glad that you decided to join!  Below, you will see the information about who you are going to be buying a gift for.

{%+ if data.gift_receiver.instagram|length %}
Instagram Account: @{{ data.gift_receiver.instagram }}
{%- endif %}
{%+ if data.gift_receiver.address|length %}
Delivery Details:  {{ data.gift_receiver.address }}
{%- endif %}
{%+ if data.gift_receiver.other|length %}
Any extra information: {{ data.gift_receiver.other }}
{%- endif %}

As explained already, the plan is to buy a gift online and have it delivered to the other person’s address.  Our budget will be €20.  Please try your best to buy something that will be delivered to your teacher by the end of the month.

When you receive your gift in the post, please share a photo on Instagram using the hashtag #muinteoirgift and tag the person who sent it to you as a nice “thank you”.  This gift exchange is all about spreading some fun and positivity, so I hope you all enjoy taking part!  :-)

Have a great day,

Ciara (@ciarasclassroom)

