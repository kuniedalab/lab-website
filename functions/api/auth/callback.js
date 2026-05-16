export async function onRequest(context) {
  const CLIENT_ID = context.env.GITHUB_CLIENT_ID;      // ← context.envから取得
  const CLIENT_SECRET = context.env.GITHUB_CLIENT_SECRET;  // ← context.envから取得

  const url = new URL(context.request.url);
  const code = url.searchParams.get("code");

  if (!code) {
    return new Response("Missing code", { status: 400 });
  }

  const tokenRes = await fetch("https://github.com/login/oauth/access_token", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify({
      client_id: CLIENT_ID,
      client_secret: CLIENT_SECRET,
      code,
    }),
  });

  const tokenData = await tokenRes.json();

  if (tokenData.error) {
    return new Response(`OAuth error: ${tokenData.error_description}`, {
      status: 400,
    });
  }

  const token = tokenData.access_token;
  const provider = "github";

  const script = `
    <script>
      (function() {
        function receiveMessage(e) {
          window.opener.postMessage(
            'authorization:${provider}:success:${JSON.stringify({ token, provider })}',
            e.origin
          );
        }
        window.addEventListener("message", receiveMessage, false);
        window.opener.postMessage("authorizing:${provider}", "*");
      })()
    </script>
  `;

  return new Response(script, {
    headers: { "Content-Type": "text/html" },
  });
}