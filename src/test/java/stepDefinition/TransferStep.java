package stepDefinition;

import io.cucumber.java.PendingException;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import pages.TransferPage;

public class TransferStep {

    private final TransferPage transferPage = new TransferPage();

    @Given("The user opens transfer page")
    public void openTransferPage() {
        transferPage.openPage();
    }

    @When("User selects source card Visa")
    public void SelectsSourceCard(String card) {
        transferPage.selectSourceCard(card);
    }
}