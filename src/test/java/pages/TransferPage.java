package pages;

import org.openqa.selenium.By;

import java.nio.file.Paths;

public class TransferPage extends BasePage {

    private static final String SITE_URL =
            Paths.get("src/test/resources/site/index.html").toUri().toString();

    private final By fromCard = By.id("fromCard");

    public void openPage() {
        open(SITE_URL);
    }
    public void selectSourceCard(String card){
        selectByValue(fromCard,card);
    }
}