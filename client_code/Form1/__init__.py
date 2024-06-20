from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_1.text
    age = int(self.text_box_3.text)
    emailaddress = self.text_box_2.text
    training = self.check_box_1.checked
    anvil.server.call('submit',name=name,age=age,training=training,emailaddress=emailaddress)
    Notification("Your Data Is Submitted Successfully !!").show()