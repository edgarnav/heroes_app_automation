from behave import given, when, then
from pages.MainPage import MainPage


class FavoritesSteps:


    @given("Prepare classes")
    def prepare_classes(context):
        context.main_page = MainPage(context.driver)


    @then("Verify main activity")
    def verify_main_activity(context):
        context.main_page.verify_main_activity()
