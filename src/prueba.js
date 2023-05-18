const { App } = require('@slack/bolt');
const { Configuration, OpenAIApi } = require("openai");
const { config } = require("dotenv");
const readline = require("readline");

const configuration = new Configuration({
    apiKey: "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",
  });

const openai = new OpenAIApi(configuration);


config();

const app = new App({
  token: "xoxb-1068180836245-4961980205877-wnkkAxKAAriBh2xThhvxbzkW",
  signingSecret: "83d89de0966c69ca69c4a7c5f4a93372"
});

app.message('Lio', async ({ message, say }) => {

    const question = message.text;
    const completion = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: question,
      max_tokens: 1000
      
    
    });
    console.log((("Lionel Messi ha marcado 47 goles desde af").length))
    console.log(completion)
    
  await say(`${completion.data.choices[0].text}`);
});
// <@${message.user}>!
(async () => {
  await app.start(process.env.PORT || 3000);
  console.log('Bolt app is running!');
})();