import asyncio
import asyncssh
import sys
import os


class Validator():
    def __init__(self, username, hostname):
        self.username = username
        self.hostname = hostname

    async def validate(self, user, path, entrypoint_type):
        print(f'Validating {path} ({entrypoint_type})')

        try:
            response = await self._get_conda_envs()
            response = self._clean_response(response)

            return path in response
        except (OSError, asyncssh.Error) as exc:
            sys.exit('SSH connection failed: ' + str(exc))

    def _clean_response(self, response):
        response = response.split('\n')[2:]
        response = list(map(lambda x: x.split(' '), response))

        res = []
        for arr in response:
            tmp = list(filter(lambda x: x != '' and x != '*', arr))
            if len(tmp) > 0:
                res.append(tmp[1])
        return res

    async def _get_conda_envs(self):
        async with asyncssh.connect(self.hostname, client_keys=[f'/tmp/{self.username}.key'], username=self.username) as conn:
            response = await conn.run('conda env list', check=True)
            result = response.stdout
            return result


async def main():
    try:
        hostname = sys.argv[1]
        username = sys.argv[2]
    except:
        raise Exception('Error: missing cmd line arguments')

    v = Validator(username, hostname)

    if await v.validate('admin', '/home/admin/miniconda3/envs/test-env', 'conda'):
        print('Validation successful')
    else:
        print('Validation failed')


if __name__ == '__main__':
    asyncio.run(main())
