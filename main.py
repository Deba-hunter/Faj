import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.DesiredCapabilities;

public class WhatsAppBot {

    public static void main(String[] args) {
        // Set path to your ChromeDriver executable
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");

        // Initialize ChromeDriver
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--user-data-dir=/path/to/your/chrome/profile"); // Optional: Use your existing Chrome profile
        WebDriver driver = new ChromeDriver(options);

        try {
            // Open WhatsApp Web
            driver.get("https://web.whatsapp.com");

            // Wait for the user to scan the QR code
            System.out.println("Please scan the QR code.");
            Thread.sleep(30000); // Wait for 30 seconds for QR code scan

            // Search for the contact
            WebElement searchBox = driver.findElement(By.xpath("//div[@contenteditable='true' and @data-tab='3']"));
            searchBox.sendKeys("Contact Name"); // Replace with the contact name you want to message
            Thread.sleep(2000); // Wait for search results to load

            // Click on the contact
            WebElement contact = driver.findElement(By.xpath("//span[@title='Contact Name']")); // Replace with the contact name
            contact.click();

            // Type the message
            WebElement messageBox = driver.findElement(By.xpath("//div[@contenteditable='true' and @data-tab='6']"));
            messageBox.sendKeys("Hello! This is an automated message."); // Replace with your message
            Thread.sleep(2000);

            // Send the message
            WebElement sendButton = driver.findElement(By.xpath("//button[@class='_1E0Oz']")); // Send button
            sendButton.click();

            System.out.println("Message sent successfully!");

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // Close the browser
            driver.quit();
        }
    }
}
