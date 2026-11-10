import type { ReactNode } from "react";

export const metadata = {
  title: "DevConnect – Nền tảng chia sẻ kiến thức công nghệ",
  description:
    "Nền tảng viết và chia sẻ bài viết kỹ thuật với Markdown, Series học tập và thảo luận chuyên sâu.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="vi">
      <body className="min-h-screen bg-slate-50 text-slate-900 antialiased">
        {children}
      </body>
    </html>
  );
}
