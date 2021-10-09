function solve(object) {
    const VALID_METHODS = ['GET', 'POST', 'DELETE', 'CONNECT'];
    const VALID_VERSIONS = ['HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0'];
    const messageRegex = /^[^<\>\\\&\'\"]*$/gm;
    const uriRegex = /^[A-Za-z0-9.]+$/gm;

    if (object.method === undefined || !VALID_METHODS.includes(object.method)) {
        throw new Error('Invalid request header: Invalid Method');
    }

    if (object.uri === undefined || object.uri.match(uriRegex) === null && object.uri !== '*') {
        throw new Error('Invalid request header: Invalid URI');
    }

    if (object.version === undefined || !VALID_VERSIONS.includes(object.version)) {
        throw new Error('Invalid request header: Invalid Version');
    }

    if (object.message === undefined || object.message.match(messageRegex) === null) {
        throw new Error('Invalid request header: Invalid Message');
    }

    return object;
}

solve({
    method: 'GET',
    uri: 'svn.public.catalog',
    version: 'HTTP/1.1',
    message: ''
});