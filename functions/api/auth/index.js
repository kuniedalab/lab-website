const CLIENT_ID = GITHUB_CLIENT_ID;

export async function onRequest(context) {
  const url = new URL(context.request.url);
  const base = `${url.protocol}//${url.host}`;

  const params = new URLSearchParams({
    client_id: CLIENT_ID,
    redirect_uri: `${base}/api/auth/callback`,
    scope: "repo,user",
    state: crypto.randomUUID(),
  });

  return Response.redirect(
    `https://github.com/login/oauth/authorize?${params}`,
    302
  );
}