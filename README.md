# 🚫 Wi-Fi Device Blocker Guide 🚀

👋 Hello there! This guide will help you (attempt to) restrict a device from using your Hathway Wi-Fi network. ⚠️ **Disclaimer:** This is not a foolproof method, and effectiveness may vary! We'll cover both the recommended (router interface) and the less reliable (command prompt) approaches.

## ⚠️ IMPORTANT! ⚠️

*   **Read this entire README before you start!**
*   **Router Access Needed:** You *must* know your router's IP address, username, and password.
*   **Device ID:** You *must* know the MAC address of the device you want to block.
*   **Hathway Variations:** Exact steps will vary slightly based on your Hathway router model.
*   **Admin Rights:** You need administrator privileges on your laptop.
*   **Security:** Change your Wi-Fi and router passwords after making changes!

## 💻 Part 1: Gathering Info 🔍

### 1.  Find Your Router's IP Address (Gateway)

This is the address you'll type into your web browser to access your router's settings.

*   **Windows (Command Prompt):**

    ```cmd
    ipconfig
    ```

    Look for "Default Gateway" in the output.  It will look like `192.168.1.1` or `192.168.0.1`.

    <details>
    <summary>Windows ipconfig example (click to expand)</summary>

    ```
    Windows IP Configuration


    Ethernet adapter Ethernet:

       Connection-specific DNS Suffix  . :
       Link-local IPv6 Address . . . . . : fe80::xxxx:xxxx:xxxx:xxxx%4
       IPv4 Address. . . . . . . . . . . : 192.168.1.100
       Subnet Mask . . . . . . . . . . . : 255.255.255.0
       Default Gateway . . . . . . . . . . : 192.168.1.1
    ```

    </details>

*   **macOS (Terminal):**

    ```bash
    netstat -nr | grep default
    ```

    The IP address next to "default" is your router's IP.

    <details>
    <summary>macOS netstat example (click to expand)</summary>

    ```
    default            192.168.1.1        UGScg           13      0 en0
    ```

    </details>

*   **Linux (Terminal):**

    ```bash
    route -n
    ```

    Look for the "Gateway" entry associated with the destination `0.0.0.0`.

    <details>
    <summary>Linux route example (click to expand)</summary>

    ```
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    0.0.0.0         192.168.1.1     0.0.0.0         UG    0      0        0 wlan0
    ```

    </details>

### 2. Find the MAC Address of the Device to Block

The MAC address is a unique identifier for the device's network interface.  It's crucial for blocking!

*   **On the Device Itself (Easiest):**

    *   **Windows:**  `ipconfig /all` (Command Prompt), look for "Physical Address" under the Wi-Fi adapter.
    *   **macOS:** System Preferences > Network > Wi-Fi > Advanced > Hardware.  "MAC Address".
    *   **Android:** Settings > About phone > Status > Wi-Fi MAC address (location varies by Android version).
    *   **iOS (iPhone/iPad):** Settings > General > About > Wi-Fi Address.
        <br>
       It will look like : `00:1A:2B:3C:4D:5E`.

*   **From Your Router's Interface (Recommended if you can't access the device):**

    Log into your router (see Part 2) and look for sections like:

    *   "Attached Devices"
    *   "DHCP Clients"
    *   "Wireless Clients"

    These sections usually list connected devices and their MAC addresses.

## 🔑 Part 2: Accessing Your Router's Web Interface 🌐

1.  **Open a Web Browser:** Chrome, Firefox, Safari, Edge, etc.

2.  **Enter Your Router's IP Address:** Type the IP address you found in Part 1 into the address bar and press Enter.

3.  **Log In:** 🔑 You'll be prompted for a username and password. This is *not* your Wi-Fi password. It's the admin password for the router!

    *   **Default Credentials:**  If you've never changed it, try:
        *   Username: `admin` or blank
        *   Password: `admin`, `password`, blank, or the router's serial number (look on the router itself).

    *   **Forgotten Password?** 😱 Consult your router's documentation, the Hathway website, or contact Hathway support. You might have to reset the router to factory defaults (but this will erase *all* your settings!). Only do this as a last resort.

## 🛡️ Part 3: Blocking the Device (MAC Filtering) 🚫

This is where it gets specific to *your* Hathway router model. 🕵️ Search for these sections in your router's interface:

*   **MAC Filtering** (most common)
*   **Wireless MAC Address Filter**
*   **Access Control**
*   **Parental Controls** (sometimes hidden here!)
*   **Wireless Security**

Once you find the right section:

1.  **Enable MAC Filtering:** Check the "Enable" box or similar. ✅

2.  **Choose Allow or Deny List:**

    *   **Allow List (Whitelist):**  Only devices with listed MAC addresses can connect.  *More secure, but requires you to add every authorized device.*
    *   **Deny List (Blacklist):** Devices with listed MAC addresses are blocked.  *Easier to set up for blocking one device, but less secure overall.*

3.  **Add the MAC Address:** Enter the MAC address you found in Part 1. Give it a description if prompted (e.g., "John's Phone").

4.  **Save/Apply:** Click "Save," "Apply," or "Submit." Your router may reboot. 🔄

## 💥 Part 4: The (Less Reliable) Command Prompt Method 🪤

⚠️ **This is unlikely to work permanently on Wi-Fi.**  It's a temporary fix at best.

1.  **Find the Device's IP Address:** Use your router or a network scanner (like `nmap`) to find the IP address assigned to the device.

2.  **Clear ARP Entry (Temporary):**

    *   Open Command Prompt (as Administrator!).
    *   Type:

        ```cmd
        arp -d <device's IP address>
        ```

        Example: `arp -d 192.168.1.105`

### Why this is unreliable:

*   **Temporary:** The ARP table will be repopulated, and the device will reconnect.
*   **Local Effect Only:** It only affects *your* computer, not the router.
*   **Limited Control:**  Not a permanent block.
*   **Often Ineffective:** Modern networks make this hard to do

## 🚑 Troubleshooting 🆘

*   **Can't Access Router?**

    *   Double-check the IP address. 🧐
    *   Make sure you're connected to the Wi-Fi. 📶
    *   Try restarting the router. 🔌

*   **Incorrect MAC Address?**

    *   Double-check! A typo will break everything. ⌨️

*   **Router Interface Different?**

    *   Consult your router's manual or the Hathway website. 📚

*   **Device Still Connecting?**

    *   The device might have a static IP address. Try blocking the IP address in addition to the MAC address (if supported).
    *   The device might be using a VPN. 🛡️ VPNs make it harder to block devices effectively.

## 🌟 Conclusion ✨

The **best and most reliable method** is using MAC address filtering through your router's web interface. The command prompt method is a temporary and often ineffective workaround.  Good luck! 👍

```javascript
// this section does not run as it needs to be in a js file

// An example of a simple javascript animation
function animateText(elementId) {
  const element = document.getElementById(elementId);
  if (!element) return;

  let opacity = 0;
  const fadeIn = setInterval(() => {
    opacity += 0.05;
    if (opacity >= 1) {
      clearInterval(fadeIn);
      opacity = 1;
    }
    element.style.opacity = opacity;
  }, 50);
}

// Call this function with the ID of an element to animate it when the page loads
// Example: animateText('readme-title');
