# <span style="color:pink">Assignment</span>

## <span style="color:red">What in Assignment</span>

1. [Online vs Offline Extraction](#online-vs-offline-extraction)
    - [Definition](#definition)
    - [Online Extraction](#online-extraction)
    - [Offline Extraction](#offline-extraction)
    - [Similarity](#similarity)
    - [Difference](#difference)

2. [ETL vs ELT](#etl-vs-elt)
    - [Definition](#definition-1)
    - [ETL](#etl)
    - [ELT](#elt)
    - [Similar](#similar-1)
    - [Difference](#difference-1)

3. [Virtual Environment vs Virtual Machine vs Container](#ve-vm-con)
    - [Virtual Environment](#ve)
    - [Virtual Machine](#vm)
    - [Container](#con)
    - [Similar](#similar-2)
    - [Difference](#difference-2)


## <span id = "online-vs-offline-extraction" style="color:red">Online vs Offline Extraction</span>
### <span id = "definition" style="color:yellow">Definition</span>
- <span style="color:green">Online Extraction</span> : Typically refers to the process of retrieving specific information or data from a digital source in real-time or near-real-time. It involves extracting relevant data from various online platforms, such as websites, databases, social media, or any other digital sources where information is stored or updated regularly.

- <span style="color:green">Offline Extraction</span> : Refers to the process of retrieving specific information or data from sources that are not directly connected to the internet or are not actively updated in real-time. Unlike online extraction, which involves accessing digital sources in real-time or near-real-time, offline extraction involves accessing data that has been previously stored or collected and is typically static or updated less frequently.

### <span id = "online-extraction" style="color:yellow">Online Extraction</span>
- <span style="color:green">**Characteristics**</span>

    - **Automation**: Online extraction is typically automated, utilizing scripts or software tools to gather data from websites.
    - **Scalability**: It can be scaled up to handle large volumes of data from multiple sources simultaneously.
    - **Customizability**: Extraction scripts can be tailored to specific websites and data structures, allowing for precise data collection.
    - **Real-time Data**: Online extraction enables the retrieval of real-time or up-to-date information from websites.
    - **Wide Range of Data**: It can extract various types of data including text, images, links, and more, depending on the requirements.

- <span style="color:green">**Advantages**</span>

    - **Time Efficiency**: Online extraction automates the data collection process, saving time compared to manual data entry or copy-pasting.
    - **Cost-effectiveness**: It reduces the need for manual labor, thus cutting down on operational costs.
    - **Data Accuracy**: When configured correctly, online extraction can yield accurate and consistent data, minimizing human error.
    - **Competitive Intelligence**: It allows businesses to monitor competitors, industry trends, and market dynamics by collecting relevant data from competitor websites.
    - **Research and Analysis**: Online extraction provides valuable data for research, analysis, and decision-making purposes in various fields such as market research, academic studies, and business intelligence.

- <span style="color:green">**Disadvantages**</span>

    - **Legality Concerns**: The legality of web scraping is a gray area and can vary depending on factors such as the website's terms of service and the purpose of data extraction.
    - **Ethical Consideration**: Scraping data from websites without permission may raise ethical concerns, especially if it involves personal or sensitive information.
    - **Data Quality Issues**: Websites may change their structure or content layout, leading to data extraction errors or inconsistencies.
    - **IP Blocking**: Websites can detect and block automated extraction activities, leading to IP bans or restrictions.
    - **Maintenance Overhead**: Online extraction scripts may require regular updates and maintenance to adapt to changes in website layouts or security measures.
##### [Link direct to online extraction code github](https://github.com/hhtrieu0108/assignment_27052024/tree/main/online_extraction)
#### Flowchart :
![Flowchart](online_extraction.png)


### <span id = "offline-extraction" style="color:yellow">Offline Extraction</span>
- <span style="color:green">**Characteristics**</span>
    - **Localized Data**: Offline extraction retrieves data from local sources such as databases, files, or documents stored on a device or within a network.
    - **Manual or Semi-Automated**: Unlike online extraction, which is typically automated, offline extraction may involve manual or semi-automated processes to gather data.
    - **Security**: Since offline extraction deals with data stored locally, it may offer higher security compared to online extraction, especially when handling sensitive information.
    - **Control**: Users have more control over the extraction process and can manage data storage and access according to their requirements.
    - **Data Integrity**: Offline extraction may ensure data integrity since the data source is not subject to changes or updates from external sources.

- <span style="color:green">**Advantages**</span>
    - **Data Privacy**: Offline extraction can be preferable when dealing with sensitive or confidential information since it does not involve transmitting data over the internet.
    - **Stability**: Since offline data sources are not subject to internet connectivity issues or website changes, the extraction process may be more stable and predictable.
    - **Compliance**: Offline extraction may align better with data privacy regulations and compliance requirements since it does not involve accessing external websites or servers.
    - **Customizability**: Users have more flexibility to customize the extraction process according to their specific needs and preferences.
    - **Performance**: Offline extraction can be faster and more reliable compared to online extraction, especially when dealing with large volumes of data stored locally.

- <span style="color:green">**Disadvantages**</span>
    - **Limited Data Scope**: Offline extraction is constrained to the data available in local sources, which may limit the breadth and depth of information compared to online sources.
    - **Data Staleness**: Offline data may become outdated over time if not regularly updated or synchronized with external sources.
    - **Resource Intensive**: Extracting data from local sources may require significant computing resources, especially when dealing with large databases or complex data structures.
    - **Initial Setup Complexity**: Setting up offline extraction processes, such as connecting to databases or configuring data extraction tools, may require technical expertise and effort.
    - **Dependency on Local Infrastructure**: Offline extraction relies on local infrastructure and systems, making it vulnerable to hardware failures, software errors, or network issues.

##### [Link direct to offline extraction code github](https://github.com/hhtrieu0108/assignment_27052024/tree/main/offline_extraction)
#### Flowchart :
![Flowchart](offline_extraction.png)

### <span id = "similarity" style="color:yellow">Similarity</span>

- **Data Collection**: Both online and offline extraction methods involve the collection of data for various purposes such as analysis, research, or business intelligence.
- **Data Processing**: After extraction, data obtained through both methods may undergo further processing, such as cleaning, transformation, or analysis, depending on the specific requirements.
- **Data Source**: Ultimately, both methods aim to acquire data, albeit from different sources. Online extraction focuses on retrieving data from websites or online sources, while offline extraction gathers data from local databases, files, or physical documents.

### <span id = "difference" style="color:yellow">Difference</span>

| Aspect               | Online Extraction                                          | Offline Extraction                                         |
|----------------------|------------------------------------------------------------|-------------------------------------------------------------|
| Connectivity         | Requires active internet connection for data retrieval     | Does not require internet connectivity for data retrieval   |
| Automation           | Typically automated using scripts, bots, or software tools | May involve manual or semi-automated processes              |
| Real-time Data       | Enables retrieval of real-time or up-to-date information  | May capture static snapshots of data unless regularly updated|
| Security and Privacy| Raises concerns about data privacy and legality            | Offers advantages in data security and privacy              |
| Scalability         | Can be scaled up for extensive data collection             | May have limitations in scalability                         |

## <span id = "etl-vs-elt" style="color:red">ETL vs ELT</span>
### <span id = "definition-1" style="color:yellow">Definition</span>

- <span style="color:green">ETL</span> : Stand for Extract, Transform and Load.ETL is a process that involves extracting data from various sources, transforming it to fit operational needs, and loading it into a target destination such as a data warehouse or database.
- <span style="color:green">ELT</span> : Stand for Extract, Load and Transform.ELT refers to the process of extracting data from various sources, loading it into a target destination (usually a data warehouse), and then transforming it within the destination system. Unlike ETL, where transformation occurs before loading into the destination, ELT loads the data first and performs transformations within the target system using its processing capabilities.

### <span id = "etl" style="color:yellow">ETL</span>
- <span style="color:green">**Characteristics**</span>

    - **Sequential Process**: ETL follows a sequential process where data is first extracted from the source systems, then transformed according to the target schema, and finally loaded into the destination.
    - **Transformation-Centric**: The emphasis is on transforming the data before loading it into the target system. This involves data cleansing, aggregation, normalization, and other operations to prepare the data for analysis.
    - **Structured Data Handling**: ETL is well-suited for structured data environments where data is organized in predefined schemas, such as relational databases.
    - **Separation of Concerns**: It separates the extraction, transformation, and loading processes, allowing for easier management and maintenance of each stage individually.

- <span style="color:green">**Advantages**</span>

    - **Data Quality**: ETL processes facilitate data cleansing and standardization, improving data quality before it's loaded into the target system.
    - **Performance Optimization**: Transforming data before loading can optimize performance by reducing the amount of data transferred and ensuring it aligns with the target schema.
    - **Security**: ETL processes can incorporate data security measures during the transformation phase, ensuring sensitive information is protected before loading.
    - **Historical Data Handling**: ETL processes are well-suited for historical data integration, allowing for complex transformations and historical comparisons.

- <span style="color:green">**Disadvantages**</span>
    - **Complexity**: ETL processes can be complex and time-consuming to design and implement, especially for large-scale data integration projects.
    - **Processing Overhead**: Transformation processes can introduce processing overhead, potentially slowing down the overall data integration process.
    - **Latency**: Due to the sequential nature of ETL, there can be latency between data extraction and availability in the target system, which may not be suitable for real-time analytics.

### <span id="elt" style="color:yellow">ELT</span>
- <span style="color:green">**Characteristics**</span>

    - **Parallel Processing**: ELT processes extract data from source systems and load it into the target system without immediate transformation, enabling parallel processing and scalability.
    - **Schema-on-Read**: Data is loaded into the target system in its raw form, and transformations are applied as needed when querying the data, allowing for flexible schema design.
    - **Big Data Compatibility**: ELT is well-suited for big data environments where data volumes are massive and traditional transformation approaches may not be feasible.
    - **Real-time Analytics**: ELT can support real-time analytics by loading raw data quickly and applying transformations on-the-fly during analysis.

- <span style="color:green">**Advantages**</span>

    - **Scalability**: ELT processes can scale horizontally to handle large volumes of data by leveraging distributed computing frameworks.
    - **Flexibility**: Schema-on-read allows for flexibility in data exploration and analysis, as transformations are applied dynamically during query execution.
    - **Cost-Efficiency**: ELT processes can be cost-effective, especially in cloud environments, as they leverage the storage and processing capabilities of cloud platforms.
    - **Real-time Insights**: By loading data quickly and applying transformations during analysis, ELT enables real-time insights and decision-making.

- <span style="color:green">**Disadvantages**</span>

    - **Data Quality Challenges**: Loading raw data without immediate transformation can lead to data quality issues if proper cleansing and validation measures are not applied during analysis.
    - **Complex Querying**: ELT may require more complex querying and analysis tools to handle raw data and apply transformations dynamically, which can increase complexity for end-users.
    - **Resource Intensive**: ELT processes may require significant computational resources, especially during data analysis and transformation stages, which can impact performance and cost.
    - **Security Concerns**: Loading raw data into the target system may raise security concerns, as sensitive information is stored without immediate transformation, requiring robust access control measures.

### <span id = "similarity-1" style="color:yellow">Similarity</span>
- **Data Integration**: Both ETL and ELT are methodologies used to integrate data from multiple sources into a single destination, typically a data warehouse or data lake.
- **Automation**: Both processes can be automated using various tools and platforms to streamline the movement and transformation of data.
- **Scalability**: Both ETL and ELT processes can handle large volumes of data and can scale according to the needs of the organization.

### <span id = "difference-1" style="color:yellow">Difference</span>
| Aspect               | ETL                                    | ELT                                    |
|----------------------|----------------------------------------|----------------------------------------|
| Sequence of Operations | Extract, Transform, Load               | Extract, Load, Transform               |
| Transformation Location | Transformation occurs outside the target system, typically in a separate ETL environment | Transformation occurs within the target system, leveraging its processing power and capabilities |
| Scalability          | May face scalability challenges, as transformation occurs before loading into the target system | Can be more scalable, as transformation occurs within the target system, which can often be scaled out horizontally |
| Data Processing Requirements | Suitable for scenarios where significant data transformation is required before loading into the target system | Suitable for scenarios where the target system has sufficient processing power and capabilities to handle raw data and perform transformations as needed |


## <span id = "ve-vm-con" style="color:red">Virtual Environment vs Virtual Machine vs Container</span>
### <span id = "definition-2" style="color:yellow">Definition</span>
- <span style="color:green">Virtual Environment </span> : A virtual environment is a self-contained environment where software can run in isolation from the rest of the system. It typically includes a specific version of a programming language interpreter (like Python), along with a set of libraries and dependencies required for a particular project or application. Virtual environments are commonly used in software development to manage dependencies and ensure consistency across different projects or deployments. Tools like virtualenv for Python or venv (built-in with Python 3) are used to create and manage virtual environments.

- <span style="color:green">Virtual Machine</span> : A virtual machine is an emulation of a physical computer system, capable of running an operating system (OS) and applications just like a physical machine. However, it runs on top of a physical host machine through a hypervisor, which provides the necessary virtualization capabilities. Each virtual machine is isolated from other VMs running on the same host, allowing multiple operating systems and applications to run on a single physical machine simultaneously. VMs are widely used for server virtualization, cloud computing, software testing, and development environments.

- <span style="color:green">Container</span> : A container is a lightweight, portable, and self-sufficient software package that includes everything needed to run an application, such as code, runtime, system tools, libraries, and settings. Containers provide a consistent environment across different platforms and ensure that the application behaves the same way regardless of where it's deployed. Unlike virtual machines, containers share the host OS kernel but are isolated from each other using containerization technologies like Docker or Kubernetes. Containers offer advantages such as faster startup times, efficient resource utilization, and scalability, making them popular for deploying microservices, building cloud-native applications, and continuous integration/continuous deployment (CI/CD) pipelines.

### <span id = "ve" style="color:yellow">Virtual Environment</span>
- <span style="color:green">**Characteristics**</span>

    - **Isolation**: Virtual environments isolate dependencies and configurations, preventing conflicts between different projects or applications.
    - **Lightweight**: They are lightweight compared to virtual machines and containers since they don't require a full OS virtualization.
    - **Dependency Management**: Virtual environments allow for the management of specific versions of programming language runtimes, libraries, and dependencies.
    - **Portability**: They can be easily shared and replicated, ensuring consistent development environments across different systems.

- <span style="color:green">**Advantages**</span>

    - **Dependency Control**: Provides fine-grained control over dependencies, ensuring that projects use the required versions without affecting the system-wide environment.
    - **Ease of Use**: Virtual environments are relatively easy to set up and manage, making them accessible for developers of various skill levels.
    - **Resource Efficiency**: They consume fewer resources compared to virtual machines since they don't require a separate OS instance.

- <span style="color:green">**Disadvantages**</span>

    - **Limited Isolation**: Virtual environments may not provide complete isolation from the host system, leading to potential compatibility issues.
    - **Limited Scalability**: They may not scale well for deploying large-scale applications or services.
    - **Complexity**: Managing multiple virtual environments across different projects can become complex and cumbersome.

### <span id="vm" style="color:yellow">Virtual Machine</span>
- <span style="color:green">**Characteristics**</span>

    - **Full OS Virtualization**: Virtual machines emulate complete hardware environments, including a full OS instance, allowing for the deployment of multiple OS environments on a single physical machine.
    - **Isolation**: VMs provide strong isolation between different instances, making them suitable for running multiple applications with diverse requirements.
    - **Resource Allocation**: VMs allow for fine-grained control over resource allocation, such as CPU, memory, and storage.

- <span style="color:green">**Advantages**</span>

    - Strong Isolation: VMs offer strong isolation, ensuring that applications running on one VM do not impact others.
    - Versatility: VMs support running different operating systems, making them suitable for a wide range of applications and use cases.
    - Security: VMs can enhance security by sandboxing applications and providing isolation from the host system.

- <span style="color:green">**Disadvantages**</span>

    - **Resource Overhead**: VMs incur significant resource overhead due to the need to run a separate OS instance for each VM.
    - **Slow Startup**: VMs typically have slower startup times compared to containers due to the time required to boot the OS.
    - **Complexity**: Managing VMs involves additional complexity, including managing hypervisors, OS updates, and patches.

### <span id="con" style="color:yellow">Container</span>
- <span style="color:green">**Characteristics**</span>

    - **OS-Level Virtualization**: Containers share the host OS kernel while providing isolated filesystems, processes, and network interfaces.
    - **Lightweight**: Containers are lightweight compared to VMs since they don't require separate OS instances, resulting in faster startup times and lower resource overhead.
    - **Portability**: Containers are highly portable and can run consistently across different environments, including development, testing, and production.

- <span style="color:green">**Advantages**</span>

    - **Resource Efficiency**: Containers consume fewer resources compared to VMs, making them highly efficient for deploying and scaling applications.
    - **Scalability**: Containers scale easily, allowing for rapid deployment and scaling of applications to meet changing demands.
    - **onsistency**: Containers provide consistent runtime environments, ensuring that applications behave the same way regardless of the underlying infrastructure.

- <span style="color:green">**Disadvantages**</span>

    - **Security**: While containers offer isolation, vulnerabilities in the host kernel or container runtime can potentially compromise the security of all containers on the host.
    - **Limited OS Support**: Containers rely on the host OS kernel, limiting the range of supported operating systems compared to VMs.
    - **Orchestration Complexity**: Managing containerized applications at scale requires additional tools and frameworks for orchestration, such as Kubernetes, which can introduce complexity.

### <span id = "similarity-2" style="color:yellow">Similarity</span>

- **Isolation**: All three technologies provide a form of isolation for running software, ensuring that applications and their dependencies are encapsulated and do not interfere with each other or the host system.
- **Dependency Management**: They all offer a way to manage dependencies and software configurations, allowing for the installation of specific versions of libraries, frameworks, and runtime environments.
- **Portability**: Virtual environments, virtual machines, and containers are all portable, meaning they can be easily moved or deployed across different systems or environments, providing consistency for development, testing, and deployment.

### <span id = "difference-2" style="color:yellow">Difference</span>
| Feature             | Virtual Environment                                       | Virtual Machine                                            | Container                                                    |
|---------------------|-----------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------|
| Level of Abstraction | Operates at the level of the programming language runtime. | Emulates complete hardware environments, including a full OS. | Operates at the OS-level, sharing the host OS kernel.         |
| Resource Overhead   | Typically lightweight, as they don't require full OS virtualization. | Incurs significant resource overhead due to running separate OS instances. | Lightweight, shares the host OS kernel, resulting in minimal overhead. |
| Performance         | Provides good performance, with minimal overhead.         | Performance can vary depending on the workload and hypervisor. | Offers excellent performance due to minimal overhead and efficient resource utilization. |
| Isolation Level     | Provides isolation at the programming language runtime level, preventing conflicts between different projects or applications. | Offers strong isolation, emulating complete hardware environments and providing separate OS instances for each VM. | Provides lightweight isolation, sharing the host OS kernel while ensuring each container has its own isolated filesystem, processes, and network interfaces. |
| Security            | Provides limited security, as isolation is at the programming language runtime level. | Offers strong security, with each VM running its own OS instance and having limited access to the host system. | Provides moderate security, with isolation at the OS level, but vulnerabilities in the host kernel or container runtime can impact security. |

