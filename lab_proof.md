

**news_api**
(/Users/nevena/Ironhack_Labs/.conda) nevena@Nevenas-MBP-2 LAB8_Two_Brains % python news_api.py

Latest Technology News

1. The New Mercedes-Maybach GLS Debuts With More Power, Better Style - Motor1.com
   Source: Motor1 
   Description: Mercedes-Benz has unveiled the 2027 Maybach GLS 680, which now has a more powerful twin-turbocharged V8 engine and an updated design. These are the details.
   URL: https://www.motor1.com/news/802238/2027-mercedes-maybach-gls-680-engine-specs-details/

2. iOS 27 beta 4 adds a useful Apple TV app feature, here’s how it works - 9to5Mac
   Source: 9to5Mac
   Description: Apple released iOS 27 beta 4 today, and it comes with a useful new “Automatic Downloads” feature in the Apple...
   URL: https://9to5mac.com/2026/07/20/ios-27-beta-4-adds-a-useful-apple-tv-app-feature-heres-how-it-works/

3. A mathematician used Fable 5 to disprove a major math problem - Mashable
   Source: Mashable
   Description: The Jacobian conjecture has bedeviled math experts for nearly 90 years.
   URL: https://mashable.com/tech/anthropic-fable-5-disproves-jacobian-conjecture






**llm_providers**
(/Users/nevena/Ironhack_Labs/.conda) nevena@Nevenas-MBP-2 LAB8_Two_Brains % python llm_providers.py

=== Testing OpenAI ===
Automation workflows are useful because they streamline repetitive tasks, increase efficiency, reduce errors, and free up time for more strategic activities.

Provider: OpenAI
Input tokens: 30
Output tokens: 25


=== Testing Cohere ===
Sending request to Cohere...
Cohere response received
Automation workflows streamline repetitive tasks, saving time and reducing errors by allowing systems to execute processes without manual intervention.

Provider: Cohere



**summarizer**

(/Users/nevena/Ironhack_Labs/.conda) nevena@Nevenas-MBP-2 LAB8_Two_Brains % python summarizer.py
Fetching news articles...

Processing: The New Mercedes-Maybach GLS Debuts With More Power, Better Style - Motor1.com

Summary:
Mercedes-Benz has revealed the 2027 Maybach GLS 680, featuring a more powerful twin-turbocharged V8 engine that enhances its performance. The luxury SUV also sports an updated design, emphasizing both elegance and modernity.

Sentiment:
Positive

Processing: Donkey Kong Arcade LEGO Set Official Images Surface, Already In-Store - nintendolife.com

Summary:
Official images of the Donkey Kong Arcade LEGO set have been released, revealing detailed designs that faithfully recreate the classic arcade game. The set is already available for purchase in stores, allowing fans to build and display a nostalgic piece of gaming history. This launch highlights a growing trend of iconic video game franchises being celebrated through LEGO collaborations.

Sentiment:
Neutral

=== Cost Summary ===
Input tokens: 128
Output tokens: 111


**test**

(/Users/nevena/Ironhack_Labs/.conda) nevena@Nevenas-MBP-2 LAB8_Two_Brains % pytest test_summarizer.py -v
=========================================== test session starts ============================================
platform darwin -- Python 3.12.12, pytest-9.1.1, pluggy-1.6.0 -- /Users/nevena/Ironhack_Labs/.conda/bin/python3.12
cachedir: .pytest_cache
rootdir: /Users/nevena/Ironhack_Labs/week3/LAB8_Two_Brains
plugins: anyio-4.14.2
collected 2 items                                                                                          

test_summarizer.py::test_summarize_article PASSED                                                    [ 50%]
test_summarizer.py::test_cost_summary PASSED                                                         [100%]

============================================ 2 passed in 0.61s =============================================


**main**
(/Users/nevena/Ironhack_Labs/.conda) nevena@Nevenas-MBP-2 LAB8_Two_Brains % python main.py

=== News Summarizer ===

Fetching technology news...

--------------------------------
Processing: The New Mercedes-Maybach GLS Debuts With More Power, Better Style - Motor1.com

Summary:
Mercedes-Benz has introduced the 2027 Maybach GLS 680, featuring a more powerful twin-turbocharged V8 engine and an updated design. The luxury SUV showcases enhanced performance alongside refreshed aesthetics.

Sentiment:
Positive

--------------------------------
Processing: Donkey Kong Arcade LEGO Set Official Images Surface, Already In-Store - nintendolife.com

Summary:
Official images of the Donkey Kong Arcade LEGO set have been revealed, showcasing a detailed and nostalgic design based on the classic arcade game. The set is already available for purchase in stores, allowing fans to build and display a miniature version of the iconic arcade cabinet.

Sentiment:
Positive

=== Cost Summary ===
Input tokens: 128
Output tokens: 92
