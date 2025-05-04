output of `example.py`:

### model: gpt-4.1-nano-2025-04-14

```
---------- TextMessage (user) ----------
What is the weather in New York?
---------- ToolCallRequestEvent (weather_agent) ----------
[FunctionCall(id='call_zgrHrPsz5oEy9q0kd6ywnYpq', arguments='{"city":"New York"}', name='get_weather')]
---------- ToolCallExecutionEvent (weather_agent) ----------
[FunctionExecutionResult(content='The weather in New York is 73 degrees and Sunny.', name='get_weather', call_id='call_zgrHrPsz5oEy9q0kd6ywnYpq', is_error=False)]
---------- ModelClientStreamingChunkEvent (weather_agent) ----------
The weather in New York is 73 degrees and sunny.
```


### model: gemini-2.5-flash-preview-04-17

```
---------- TextMessage (user) ----------
What is the weather in New York?
---------- ToolCallRequestEvent (weather_agent) ----------
[FunctionCall(id='', arguments='{"city":"New York"}', name='get_weather')]
---------- ToolCallExecutionEvent (weather_agent) ----------
[FunctionExecutionResult(content='The weather in New York is 73 degrees and Sunny.', name='get_weather', call_id='', is_error=False)]
---------- ModelClientStreamingChunkEvent (weather_agent) ----------
The weather in New York is 73 degrees and Sunny.
```

### model: qwen3-30b-a3b (ran locally)
```
---------- TextMessage (user) ----------
What is the weather in New York?
---------- ModelClientStreamingChunkEvent (weather_agent) ----------
<think>
Okay, the user is asking for the weather in New York. Let me check the tools available. There's a function called get_weather that takes a city parameter. So I need to call that function with "New York" as the city. I should make sure the JSON is correctly formatted with the city name. Let me structure the tool_call accordingly.
</think>


---------- ToolCallRequestEvent (weather_agent) ----------
[FunctionCall(id='123236019', arguments='{"city": "New York"}', name='get_weather')]
---------- ToolCallExecutionEvent (weather_agent) ----------
[FunctionExecutionResult(content='The weather in New York is 73 degrees and Sunny.', name='get_weather', call_id='123236019', is_error=False)]
---------- ModelClientStreamingChunkEvent (weather_agent) ----------
<think>
Okay, the user asked for the weather in New York. I used the get_weather function and got the response: 73 degrees and Sunny. Now I need to present this information clearly. Let me check if there are any specific details the user might want, but since they just asked for the weather, a straightforward answer should work. I'll mention the temperature and condition, maybe add a friendly note about enjoying the weather. Keep it simple and conversational.
</think>

The current weather in New York is **73°F** with **Sunny** conditions. A perfect day to enjoy outdoor activities! 🌞
```