# Postmortem: Nginx Port 80 Configuration Issue

## Introduction
<p>
Picture this: You’re sipping your coffee, ready to conquer the day, and suddenly, Nginx decides to take a nap. Yes, the elusive port 80 went on strike, leaving users stranded in the digital wilderness. Now, let’s dive into the epic tale of resurrecting Nginx from its slumber!
</p>

### Issue Summary
* Duration: [2023–12–18 15:00 EAT— 2023–12–18 16:30 EAT]

### Impact
* Nginx not listening on port 80.
* Users experienced service unavailability.
* Approximately 20% of users were affected.

### Root Cause
<p>
The root cause of the issue was an unintended misconfiguration in the Nginx server settings. During a routine update, a syntax error was introduced in the Nginx configuration file, causing the server to fail in binding to port 80.
</p>

### Timeline
* Issue Detected: 2023–12–18 15:00 EAT
* Detection Method: Monitoring alert triggered.

### Actions Taken
* Investigated Nginx configuration files for errors.
* Assumed misconfiguration or port conflict as potential causes.

### Misleading Paths
* Explored server memory issues but found no anomalies.
* Checked for recent changes in the Nginx config, but no relevant modifications were identified.

### Escalation
* Escalated to the DevOps team for further assistance.

### Resolution
* Configured Nginx to listen on port 80 by fixing the syntax error in the configuration file.
* Service availability was restored at 2023–12–18 16:30 EAT.

## Root Cause and Resolution
### Root Cause
<p>
I traced it back to a syntax error introduced during a routine update of the Nginx configuration file. In particular, an incomplete directive in the configuration unintentionally prevented Nginx from binding to port 80. This misconfiguration went unnoticed during the review process, leading to service disruption.
</p>

### Resolution
To address the issue, I took the following steps:

1. ___Configuration Fix___: I did a thorough review of the Nginx configuration files revealed the syntax error. The incomplete directive was identified and corrected to ensure proper server configuration.

2. ___Testing___: After fixing the configuration, Irestarted Nginx, and did an extensive testing to validate that the server could successfully bind to port 80 without any errors.

3. ___Service Restoration___: With the corrected configuration in place, service availability was restored by restarting the Nginx service at 2023–12–18 16:30 EAT.

### Resolution Explanation
1. ___Default Configuration Removal___
	- `rm /etc/nginx/sites-enabled/default`: The first step involves removing the default Nginx configuration file from the sites-enabled directory. The default configuration may conflict with the desired custom settings, and its removal ensures a clean slate for the custom configuration.

2. ___Symbolic Link Creation___
	- `ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default`: This line creates a symbolic link from the `sites-available` directory to the `sites-enabled` directory. It assumes that a custom Nginx configuration file named 'default' is present in the `sites-available` directory. The symbolic link enables this custom configuration, allowing it to take effect when Nginx is restarted.

3. ___Nginx Service Restart___
	- ___service nginx restart___: The final step involves restarting the Nginx service. This is crucial to apply the changes made in the configuration. The service restart ensures that Nginx reads the updated configuration, including the removal of the default configuration and the activation of the custom one.

### Verification and Testing
<p>
After creating and executing a custom bash script, it was essential to perform thorough testing to confirm the successful resolution:
</p>

1. ___Verify Port 80 Binding___
	- I checked if Nginx is now successfully binding to port 80 by using the command `netstat -tulpn` or `ss -tulpn` to display the active listening ports and processes.

2. ___Access the Web Application___
	- Confirmed that the web application hosted by Nginx is accessible via a web browser. Verified that users can connect to the server using the standard HTTP port (port 80).

3. ___Review Nginx Logs___
	- I examined the Nginx error logs (`/var/log/nginx/error.log`) for any issues related to the configuration changes. I later ensured there are no error messages indicating misconfiguration.

<p>
By following these detailed resolution steps and conducting thorough testing, I made sure that the Nginx port 80 configuration issue is effectively addressed.
</p>

## Corrective and Preventative Measures
### Improvements/Fixes
1. ___Patch Nginx Server___
	- Regularly update and patch the Nginx server to ensure it is running the latest stable version. This helps in addressing potential bugs, security vulnerabilities, and performance improvements. Establish a schedule for routine updates to keep the server software up-to-date.

2. ___Implement Monitoring for Server Memory___
	- Deploy a comprehensive monitoring solution to keep a close eye on server memory usage. Utilize tools like Prometheus, Grafana, or built-in system monitoring tools to set up alerts for abnormal memory patterns. Early detection of memory issues can prevent unexpected service disruptions.

### Tasks
1. ___Update Nginx Configuration___
	- Regularly review and update the Nginx configuration files, especially after system updates or changes to the web application. Establish a version control system for configuration files and maintain documentation to track modifications effectively.01~

2. ___Set Up Alerts for Port Conflicts___
	- Implement monitoring alerts specifically for port conflicts. Configure monitoring tools to notify the team if there are any changes or conflicts related to port assignments. Timely alerts can help proactively address issues before they impact service availability.

3. ___Regular Configuration Audits___
	- Conduct periodic audits of Nginx configurations to identify potential misconfigurations or syntax errors. Implement automated tools or scripts to assist in the audit process and ensure that configurations align with best practices.

4. ___Documentation and Knowledge Sharing___
	- Maintain detailed documentation outlining the server architecture, Nginx configurations, and procedures for addressing common issues. Encourage knowledge sharing within the team to ensure that insights gained from incident resolutions are disseminated.

5. ___Training and Skill Development___
	- Invest in training sessions for team members to enhance their skills in Nginx configuration management and debugging. Improved proficiency in handling Nginx issues can lead to quicker resolutions and a more resilient system.

<p>
By implementing these corrective and preventative measures, the goal is not only to address the immediate Nginx port 80 configuration issue but also to fortify the overall system against future challenges. A proactive approach to system maintenance, monitoring, and knowledge-sharing contributes to a more robust and reliable web infrastructure.
</p>

<p>
As we bid farewell to the mischievous port 80 woes, remember, even Nginx has its off days. But fear not, for armed with bash scripts and debugging prowess, I managed to triumph over the chaos. Until the next digital adventure, stay curious, stay vigilant, and may your ports always be open!
</p>
